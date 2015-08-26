from django.db import models
from fav.models import Favorite
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericRelation


class Article(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=256)
    favorites = GenericRelation(Favorite)
