from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index),
	url(r'^create$', views.create),
	url(r'^show_notes$', views.show_notes),
	url(r'^(?P<note_id>\d+)/delete$', views.delete_note)
]