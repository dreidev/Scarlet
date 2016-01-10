from django import template
from fav.forms import FavoriteForm
from fav.models import Favorite
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

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
    """
    returns whether user favorited an object or not .
    Plus a FavoriteForm of which user can alter his choice  .
    """
    positive_notation = settings.POSITIVE_NOTATION
    negative_notation = settings.NEGATIVE_NOTATION
    if Favorite.objects.filter(object_id=object.id, user=user):
        fav_value = settings.NEGATIVE_NOTATION
    else:
        fav_value = settings.POSITIVE_NOTATION
    return {"form": FavoriteForm(),
            "target": object,
            "user": user,
            "fav_value": fav_value,
            "positive_notation": positive_notation,
            "negative_notation": negative_notation}

register.inclusion_tag('fav/fav_form.html')(get_fav)


def get_fav_nouser(object, session):
    """ For non-authenticated users."""
    anonymous_permission = settings.ALLOW_ANONYMOUS
    positive_notation = settings.POSITIVE_NOTATION
    negative_notation = settings.POSITIVE_NOTATION
    if anonymous_permission == "True":
        if Favorite.objects.filter(object_id=object.id, cookie=session):
            fav_value = settings.NEGATIVE_NOTATION
        else:
            fav_value = settings.POSITIVE_NOTATION
    else:
        fav_value = settings.POSITIVE_NOTATION
        return {"form": FavoriteForm(),
                "target": object,
                "fav_value": fav_value,
                "positive_notation": positive_notation,
                "negative_notation": negative_notation,
                "cookie":session}

register.inclusion_tag('fav/fav_form.html')(get_fav_nouser)


def get_fav_count(object):
    """returns favorite count of object"""
    app_name = get_app_name(object)
    model = get_model_name(object)
    content_type = ContentType.objects.get(
        app_label=app_name,
        model=model.lower())
    try:
        fav_count = Favorite.objects.filter(
            content_type=content_type.id, object_id=object.id).count()
    except:
        fav_count = 0
    return {"fav_count": fav_count,
            "target": object}
register.inclusion_tag('fav/fav_count.html')(get_fav_count)
