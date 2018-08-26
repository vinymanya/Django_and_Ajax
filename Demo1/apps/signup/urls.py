from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^login$', views.login),
	url(r'^register$', views.register),
	url(r'^success$', views.success),
	url(r'^logout$', views.logout),
	# URL created for Ajax
	url(r'^all.json$', views.all_json),
	url(r'^all.html$', views.all_html),
	url(r'^find', views.find),
	url(r'^create$', views.create)
]