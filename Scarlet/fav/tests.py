from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from fav.models import Favorite
from test_app.models import Article
from django.conf import settings


class FavTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user(username='johndoe',
                                 password='1234')
        self.client.login(username='johndoe', password='1234')
        Article.objects.create(title="Lorem Ipsum", description="Lorem Ipsum")

    def test_fav_authenticated(self):
        """ Test favorite for authenticated users"""
        object = Article.objects.get(id=1)
        app_name = object._meta.app_label
        model_name = object.__class__.__name__
        user = User.objects.get(id=1)
        init_fav_count = Favorite.objects.count()
        response = self.client.post(
            reverse('fav-alter'),
            {
                "model": model_name,
                "model_id": object.id,
                "app_name": app_name,
                "user":  user.id,
                "fav_value": settings.POSITIVE_NOTATION,
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Favorite.objects.count(), init_fav_count + 1)

    def test_unfav_after_fav_authenticated(self):
        self.test_fav_authenticated()
        init_fav_count = Favorite.objects.count()
        object = Article.objects.get(id=1)
        app_name = object._meta.app_label
        model_name = object.__class__.__name__
        user = User.objects.get(id=1)
        response = self.client.post(
            reverse('fav-alter'),
            {
                "model": model_name,
                "model_id": object.id,
                "app_name": app_name,
                "user":  user.id,
                "fav_value": u'',
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Favorite.objects.count(), init_fav_count - 1)

    def test_fav_unauthenticated(self):
        """ Test favorite for unauthenticated users"""
        self.client.logout()
        object = Article.objects.get(id=1)
        app_name = object._meta.app_label
        model_name = object.__class__.__name__
        init_fav_count = Favorite.objects.count()
        response = self.client.post(
            reverse('fav-alter'),
            {
                "model": model_name,
                "model_id": object.id,
                "app_name": app_name,
                "user":  u'',
                "fav_value": settings.POSITIVE_NOTATION,
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Favorite.objects.count(), init_fav_count)

    def test_unfav_unauthenticated(self):
        self.test_fav_authenticated()
        self.client.logout()
        object = Article.objects.get(id=1)
        app_name = object._meta.app_label
        model_name = object.__class__.__name__
        init_fav_count = Favorite.objects.count()
        response = self.client.post(
            reverse('fav-alter'),
            {
                "model": model_name,
                "model_id": object.id,
                "app_name": app_name,
                "user":  u'',
                "fav_value": u'',
            })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Favorite.objects.count(), init_fav_count)
