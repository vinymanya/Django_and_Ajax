# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core import serializers

from .models import Lead

# Create your views here.
def index(request):
	return render(request, "leads_ajax/index.html")

# Get all leads
def all_leads(request):
	all_leads = Lead.objects.all()
	lead = Lead.objects.get(id=request.session["lead_id"])
	return render(request, "leads_ajax/all_leads.html", {"lead": lead, "all_leads": all_leads})

# Method that create leads
def create_lead(request):
	if request.method == "POST":
		errors = Lead.objects.validate_leads(request.POST)
		if len(errors):
			for field, error_msg in errors.iteritems():
				messages.error(request, error_msg, extra_tags=field)
			return redirect("/leads")
		# create a new lead
		new_lead = Lead.objects.new_lead(request.POST)
		request.session["lead_id"] = new_lead.id
		messages.success(request, "You have been successfully Added!")
		return redirect("/leads/all")
	return redirect("/leads")

# Login user
def login(request):
	if request.method == "POST":
		errors = Lead.objects.validate_login(request.POST)
		if len(errors):
			for field, error_msg in errors.iteritems():
				messages.error(request, error_msg, extra_tags=field)
			return redirect("/leads")

		result = Lead.objects.login_user(request.POST)
		request.session["lead_id"] = result.id
		messages.success(request, "You have been successfully Loggedin!")
		return redirect("/leads/all")
	return redirect("/leads")

# Logout method
def logout(request):
	request.session.clear()
	return redirect("/leads")


############################################################################
# Ajax Methods
############################################################################

def ajax_filter_name(request):
	leads = Lead.objects.filter(first_name__startswith=request.POST["name"])[:3]
	return render(request, "leads_ajax/show_leads.html", {"leads": leads})

def find(request, lead_id):
	one_lead = Lead.objects.get(id=lead_id)
	# lead = serializers.serialize("json", one_lead.first_name)
	return HttpResponse(one_lead.first_name)











