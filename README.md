#`django-ajax-favorite-like` Scarlet

`django-ajax-favorite-like` is a favoriting/liking application for Django-powered websites.

It give you the ability integrate favoriting functionality to any model you have eg. blogs, pictures, etc..

In addition, related functionalities like thumbs up, vote, like, follow are also supported.

####All actions are ajax supported.

##Installation


Installation is available via `pip`

`$ pip install django-ajax-favorite-like`

or via source on github

```
$ git clone https://github.com/dreidev/Scarlet.git
$ cd Scarlet
$ python setup.py install
```

Add 'fav' to your installed_apps in your `settings.py` file. It should look like the following. Note that you should add it after `django.contrib.auth`:

```python
INSTALLED_APPS = (
	'django.contrib.admin',
	'django.contrib.auth',
	...
	'fav',
	..
)
```

In your urls.py:

```python
urlpatterns = patterns('',
    ...
    url(r'^fav/', include('fav.urls')),
    ...
)
```


##Migrations for Django 1.7 and later


##Setup

###Step 1
In your models.py add the field comments to the model for which favorite signature should be added (e.g. Blog) and the appropriate imports as shown below

```python
from django.contrib.contenttypes.fields import GenericRelation
from fav.models import Favorite

class Blog(models.Model):
	author = models.ForeignKey(User)
	title = models.CharField(max_length=256)
	body = models.TextField()
	comments = GenericRelation(Favorite)
```

###Step 2
In your template (e.g. blog-detail.html) add the following template tags where object is the instance of blog.

```python
{% load favorite_tags %}  # Loading the template tag
{% get_fav_count object %}  # Include the number of people 'favorited' a certain object

# authentication is required for users to use our functionality, however there's an implemented tag for unauthenticated users.
example .. 
{% if user.is_authenticated %} 
{%  get_fav object user %}  # for unauthenticated users
{% else %}
{% get_fav_nouser object%} # for authenticated users
{% endif %}
```

This requires jQuery. If you're not already including it, we have a template tag that you can include in your html.
It should be added after `{%  load favorite_tags %}` directly
```python
{%  load favorite_tags %}
{% include_jQuery %}
```
 Also java script files, static, should be added for ajax to work
 ```python
{% load static %}
<script src="{% static 'js/fav.js' %}">
</script>
```


##Settings
In `settings.py` we only need to indicate which notations we would be using in our application. Wether it's favorite, like, vote, thumbs up, follow .. etc

```python
#for example .. 

POSITIVE_NOTATION = "Favorite"

NEGATIVE_NOTATION = "Unfavorite"

```
or alternatively


```python
#for example .. 

POSITIVE_NOTATION = "Follow"

NEGATIVE_NOTATION = "Unfollow"

```
###Anonymous Users

Normally unauthenticated, anonymous users are allowed to use the app's functionality .

In settings .. 

```python

ALLOW_ANONYMOUS = "TRUE"

```
to give only authenticated user this privilege this line should be omitted.
