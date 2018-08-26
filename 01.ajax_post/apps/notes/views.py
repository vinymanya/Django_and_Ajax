# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.core import serializers

from .models import Note

# Create your views here.

# Home route hanler
def index(request):
	return render(request, "notes/index.html")

def show_notes(request):
	notes = Note.objects.all().order_by("-id")
	return render(request, "notes/notes.html", {"notes": notes})

def create(request):
	note = Note.objects.create(content=request.POST["note"])
	notes = Note.objects.all().order_by("-id")
	return render(request, "notes/notes.html", {"notes": notes})

def delete_note(request, note_id):
	Note.objects.get(id=note_id).delete()
	return redirect("/notes/show_notes")



