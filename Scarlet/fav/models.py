from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import (
    GenericForeignKey)
from django.contrib.contenttypes.models import ContentType


class Favorite(models.Model):

    """ Represents an instance of Comment """

    content_type = models.ForeignKey(ContentType, null=True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')
    user = models.ForeignKey(User, null=True, blank=True)
    favorited = models.BooleanField(default=False)
