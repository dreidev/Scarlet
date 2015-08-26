from django.conf.urls import patterns, url
from views import FavCreateView

urlpatterns = patterns(
    '',
    url(
        r'^create/fav/$',
        FavCreateView.as_view(), name='fav-create'),

)
