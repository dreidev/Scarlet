from .models import Favorite
from .forms import FavoriteForm
from django.views.generic import CreateView
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse


class FavCreateView(CreateView):

    form_class = FavoriteForm
    model = Favorite
    template_name = 'fav/fav_form.html'

    def form_valid(self, form):
        fav = form.save(commit=False)
        try:
            content_type = ContentType.objects.get(
                app_label=self.request.POST['app_name'],
                model=self.request.POST['model'].lower())
            model_object = content_type.get_object_for_this_type(
                id=self.request.POST['model_id'])
            fav.content_object = model_object
            print ("object_id", model_object.id)
        except:
            pass
        favorite_object = Favorite.objects.filter(object_id=model_object.id)
        if favorite_object:
            favorite_object.delete()
        else:
            fav.save()
            return HttpResponse("Object created")
        return HttpResponse("Does  exist")
