# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Note Manager class
class NoteManager(models.Manager):
	def validate_note(self, post_data):
		errors = {}
		for field, value in post_data.iteritems():
			if field != "csrfmiddlewaretoken" and len(value) < 1:
				errors[field] = "{} field is required!".format(field)
		return errors

	# create note
	def new_note(self, post_data):
		self.create(
			title=post_data["title"], 
			desc=post_data["description"]
		)


# Create your models here.
class Note(models.Model):
	title = models.CharField(max_length=255)
	desc = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = NoteManager()
