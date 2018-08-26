# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.core import serializers

from .models import User
from functools import wraps

# Create your views here.
def index(request):
	return render(request, "signup/index.html") 


def login(request):
	if request.method == "POST":
		result = User.objects.validateLogin(request.POST) # This will either return [errors] or [user]
		if type(result) == list:
			for error in result:
				messages.error(request, error)
				return redirect("/")
				#load login the user
		request.session["user_id"] = result.id
		messages.success(request, "You have successfully logged in!")
		return redirect("/users/success")
	return redirect("/")

		
def register(request):
	if request.method == "POST":
		result = User.objects.validateRegister(request.POST)
		if type(result) == list:
			for error in result:
				messages.error(request, error)
			return redirect("/")
		request.session["user_id"] = result.id
		messages.success(request, "You have successfully registered!")
		return redirect("/users/success")
	return redirect("/")


#decorator definition
def is_logged_in(request, f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if "user_id" in request.session:
			return f(*args, **kwargs)
		else:
			messages.danger(request, "Unauthorized!, please loggin!")
			return redirect("/")
	return wrap


def success(request):
	try:
		request.session["user_id"]
	except KeyError:
		return redirect("/")
	context = {
		"user": User.objects.get(id=request.session["user_id"])
	}
	return render(request, "signup/success.html", context)


def logout(request):
	request.session.clear()
	return redirect("/")

###################################################################################
# Ajax methods
###################################################################################
def all_json(request):
	# Grab all users from db
	users = User.objects.all()
	user_json = serializers.serialize("json", users)
	return HttpResponse(user_json, content_type="application/json")

def all_html(request):
	users = User.objects.all()
	return render(request, "signup/all.html", {"users": users})

def find(request):
	users = User.objects.filter(first_name__startswith=request.POST["first_name_starts_with"])
	return render(request, "signup/all.html", {"users": users})

def create(request):
	User.objects.create(
		first_name=request.POST["first_name"], 
		last_name=request.POST["last_name"],
		email=request.POST["email"]
	)
	users = User.objects.all().order_by("-id")
	return render(request, "signup/all.html", {"users": users})



		