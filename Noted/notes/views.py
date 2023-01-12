from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Note, Tag


class NotesList(ListView):
    model = Note
    template_name = 'main.html'
    context_object_name = 'notes'


class NoteDetail(DetailView):
    model = Note
    template_name = 'note.html'
    context_object_name = 'note'


class DateList(ListView):
    model = Note
    template_name = 'date_notes.html'
    context_object_name = 'notes'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(note_time=self.kwargs['date'])
        # date = self.kwargs.get['date']
        # return Note.objects.filter(id=1)
