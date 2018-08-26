from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^create$', views.create),
	url(r'^all$', views.all_notes),
	url(r'^(?P<note_id>\d+)/update$', views.update_note),
	url(r'^(?P<note_id>\d+)/delete$', views.delete_note)
]