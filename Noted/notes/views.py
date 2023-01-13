from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Tag
from .forms import NoteForm


# выводит главную страницу с заметками на текущую неделю
class NotesList(ListView):
    model = Note
    template_name = 'main.html'
    context_object_name = 'notes'


# выводит страницу с одной заметкой
class NoteDetail(DetailView):
    model = Note
    template_name = 'note.html'
    context_object_name = 'note'


# выводит страницу с формой для добавления новой заметки
class NoteAddView(CreateView):
    template_name = 'note_add_form.html'
    form_class = NoteForm

    # это чтобы автором заметки автоматически считался текущий юзер
    def get_initial(self):
        initial = super().get_initial()
        initial['note_author'] = self.request.user
        return initial


# выводит форму для редактирования заметки
class NoteUpdateView(UpdateView):
    template_name = 'note_update_form.html'
    form_class = NoteForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Note.objects.get(pk=id)


# выводит страницу подтверждение удаления заметки
class NoteDeleteView(DeleteView):
    template_name = 'note_delete_form.html'
    queryset = Note.objects.all()
    success_url = '/main/'


# выводит страницу с заметками на конкретную дату
class DateList(ListView):
    model = Note
    template_name = 'date_notes.html'
    context_object_name = 'notes'

    # получить дату из параметра url
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(note_time=self.kwargs['date']).order_by('-note_priority')

