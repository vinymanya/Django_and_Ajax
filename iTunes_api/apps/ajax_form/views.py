# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
import requests

# Create your views here.
def index(request):
	return render(request, "ajax_form/index.html")


# Ajax method
def get_movie(request):
	# Get the user input from the Form
	artist_name = request.POST["user_input"].replace(" ", "")
	# Construct the URL using the above input value
	url = "https://itunes.apple.com/search?term="+ artist_name + "&entity=musicVideo"
	# Make an Ajax to the above URL
	response = requests.get(url).content
	return HttpResponse(response, content_type="application/json")