from django import template
from fav.forms import FavoriteForm
from fav.models import Favorite

register = template.Library()


@register.simple_tag(name='get_model_name')
def get_model_name(object):
    """ returns the model name of an object """
    return type(object).__name__


@register.simple_tag(name='get_app_name')
def get_app_name(object):
    """ returns the app name of an object """
    return type(object)._meta.app_label


def get_fav(object, user):
    # model_object = type(object).objects.get(id=object.id)
    # favs = model_object.favorites.all()
    if Favorite.objects.filter(object_id=object.id, user=user):
        fav_value = "Unfavorite"
    else:
        fav_value = "Favorite"
    return {"form": FavoriteForm(),
            "target": object,
            "user": user,
            "fav_value": fav_value}

register.inclusion_tag('fav/fav_form.html')(get_fav)


def get_fav_nouser(object):
    fav_value = "Favorite"
    return {"form": FavoriteForm(),
            "target": object,
            "fav_value": fav_value}

register.inclusion_tag('fav/fav_form.html')(get_fav_nouser)
