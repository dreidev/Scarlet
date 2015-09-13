from django.conf.urls import patterns, url
from views import FavCreateView, FavDeleteView

urlpatterns = patterns(
    '',
    url(
        r'^create/fav/$',
        FavCreateView.as_view(), name='fav-create'),
    url(
        r'^delete/fav/$',
        FavDeleteView.as_view(), name='fav-delete'),

)
