from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Note, Tag
from .forms import NoteForm


class NotesList(ListView):
    model = Note
    template_name = 'main.html'
    context_object_name = 'notes'


class NoteDetail(DetailView):
    model = Note
    template_name = 'note.html'
    context_object_name = 'note'


class NoteAddView(CreateView):
    template_name = 'note_add_form.html'
    form_class = NoteForm

    def get_initial(self):
        initial = super().get_initial()
        initial['note_author'] = self.request.user
        return initial


class DateList(ListView):
    model = Note
    template_name = 'date_notes.html'
    context_object_name = 'notes'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(note_time=self.kwargs['date'])

