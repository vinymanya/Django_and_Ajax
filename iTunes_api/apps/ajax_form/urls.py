from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^get_movie$', views.get_movie)
]