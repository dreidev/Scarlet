from .models import Favorite
from .forms import FavoriteForm
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.views.generic import DeleteView
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token


class FavCreateView(FormView):

    form_class = FavoriteForm
    model = Favorite
    template_name = 'fav/fav_form.html'

    def form_valid(self, form):
        user = authenticate(username="ahmed", password="1234")
        if user is not None:
            login(self.request, user)
        if not self.request.user.is_authenticated():
            return JsonResponse({
                'success': 0,
                'error': "You have to sign in first"})
        fav = form.save(commit=False)
        csrf_token_value = get_token(self.request)
        print "TOKEN VALUE : " + csrf_token_value
        try:
            content_type = ContentType.objects.get(
                app_label=self.request.POST['app_name'],
                model=self.request.POST['model'].lower())
            model_object = content_type.get_object_for_this_type(
                id=self.request.POST['model_id'])
            fav.content_object = model_object
        except:
            pass
        fav.save()
        return JsonResponse({"csrf": csrf_token_value})


class FavDeleteView(FormView):

    form_class = FavoriteForm
    model = Favorite
    template_name = 'fav/fav_form.html'

    def form_valid(self, form):
        csrf_token_value = get_token(self.request)
        try:
            content_type = ContentType.objects.get(
                app_label=self.request.POST['app_name'],
                model=self.request.POST['model'].lower())
            model_object = content_type.get_object_for_this_type(
                id=self.request.POST['model_id'])
        except:
            pass
        try:
            Favorite.objects.get(
                object_id=model_object.id,
                user=self.request.user,
                content_type=content_type).delete()
        except:
            pass
        return JsonResponse({"csrf": csrf_token_value})
