# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Manage leads here
class LeadManager(models.Manager):
	def validate_leads(self, post_data):
		errors = {}

		for field, value in post_data.iteritems():
			if field != "csrfmiddlewaretoken" and len(value) < 1:
				errors[field] = "{} field is required!".format(field.replace("_", " "))
			# Check for 'first_name' and 'last_name' fields
			if field == "first_name" or field == "last_name":
				if field not in errors and len(value) < 2:
					errors[field] = "{} must be at least 2 characters long!".format(field.replace("_", " "))
			# Check for a valid email address
			if field == "email":
				if field not in errors and not re.match(EMAIL_REGX, post_data["email"]):
					errors[field] = "Invalid Email address!"
				# Prevent user from registering multiple time with the same email address
				if len(self.filter(email=post_data["email"])) > 1:
					errors[field] = "Invalid email credential!"
		return errors

	# Validate the login form
	def validate_login(self, post_data):
		errors = {}
		for field, value in post_data.iteritems():
			if field != "csrfmiddlewaretoken" and len(value) < 1:
				errors[field] = "{} field is required!".format(field)
			# Check for a valid email address
			if field == "email":
				if field not in errors and not re.match(EMAIL_REGX, post_data["email"]):
					errors[field] = "Invalid Email address!"
				# Check if email exist in db
				if len(self.filter(email=post_data["email"])) == 0:
					errors[field] = "Invalid email address!"
		return errors

	# Login user
	def login_user(self, post_data): 
		user = self.filter(email=post_data["email"])[0] # [{}] or []
		return user


	# Create a new lead
	def new_lead(self, post_data):
		new_lead = self.create(
				first_name=post_data["first_name"],
				last_name=post_data["last_name"],
				email = post_data["email"]
			)
		return new_lead

# Create your models here.
class Lead(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField(unique=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = LeadManager()
