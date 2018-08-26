# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .models import Note

# Create your views here.
def index(request):
	return render(request, "notes/index.html")

# Display all notes
def all_notes(request):
	context = {
		"notes": Note.objects.all().order_by("-id")
	}
	return render(request, "notes/all_notes.html", context)

# Create a note
def create(request):
	if request.method == "POST":
		errors = Note.objects.validate_note(request.POST)
		if len(errors):
			for field, error_msg in errors.iteritems():
				messages.error(request, error_msg, extra_tags=field)
			return redirect("/notes")
		# create a note
		Note.objects.new_note(request.POST)
		notes = Note.objects.all().order_by("-id")
		return render(request, "notes/all_notes.html", {"notes": notes})
	return redirect("/notes")


# Update a note
def update_note(request, note_id):
	errors = Note.objects.validate_note(request.POST)
	if len(errors):
		for field, error_msg in errors.iteritems():
			messages.error(request, error_msg, extra_tags=field)
		return redirect("/notes/all")
	note = Note.objects.get(id=note_id)
	note.title = request.POST["title"]
	note.desc = request.POST["description"]
	note.save()
	return redirect("/notes/all")

# Delete a note
def delete_note(request, note_id):
	Note.objects.get(id=note_id).delete()
	return redirect("/notes/all")
