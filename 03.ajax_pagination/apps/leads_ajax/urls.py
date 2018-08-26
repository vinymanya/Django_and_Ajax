from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^create$', views.create_lead),
	url(r'^leads/all$', views.all_leads),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	# Ajax routes
	url(r'^ajax_filter$', views.ajax_filter_name),
	url(r'^(?P<lead_id>\d+)/find$', views.find)
]