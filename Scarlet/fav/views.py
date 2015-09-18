from .models import Favorite
from .forms import FavoriteForm
from django.contrib.contenttypes.models import ContentType
from django.http import JsonResponse
from django.views.generic.edit import FormView
from django.middleware.csrf import get_token
from django.contrib.auth import authenticate, login


class FavAlterView(FormView):

    """ alters Favorite instance 'Favorites an object' """

    form_class = FavoriteForm
    model = Favorite
    template_name = 'fav/fav_form.html'

    def form_valid(self, form):
        fav_value = self.request.POST['fav_value']
        user = authenticate(username="ahmed", password="1234")
        if user is not None:
            login(self.request, user)
        csrf_token_value = get_token(self.request)
        if fav_value == 'favorite':
            fav = form.save(commit=False)
        else:
            pass
        try:
            content_type = ContentType.objects.get(
                app_label=self.request.POST['app_name'],
                model=self.request.POST['model'].lower())
            model_object = content_type.get_object_for_this_type(
                id=self.request.POST['model_id'])
        except:
            return JsonResponse({
                'success': 0,
                'error': "You have to sign in first"})
        if fav_value == 'favorite':
            fav.content_object = model_object
            if fav.user:
                fav.save()
        else:
            Favorite.objects.get(
                object_id=model_object.id,
                user=self.request.user,
                content_type=content_type).delete()
        return JsonResponse({"csrf": csrf_token_value})
