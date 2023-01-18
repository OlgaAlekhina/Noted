from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Tag
from .forms import NoteForm


# выводит главную страницу со всеми задачами
class NotesList(ListView):
    model = Note
    template_name = 'main.html'
    context_object_name = 'notes'


# выводит страницу с одной задачей
class NoteDetail(DetailView):
    model = Note
    template_name = 'note.html'
    context_object_name = 'note'


# выводит страницу с формой для добавления новой задачи
class NoteAddView(CreateView):
    template_name = 'note_add_form.html'
    form_class = NoteForm

    # это чтобы автором задачи автоматически считался текущий юзер
    def get_initial(self):
        initial = super().get_initial()
        initial['note_author'] = self.request.user
        return initial


# выводит форму для редактирования задачи
class NoteUpdateView(UpdateView):
    template_name = 'note_update_form.html'
    form_class = NoteForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Note.objects.get(pk=id)


# выводит страницу подтверждение удаления задачи
class NoteDeleteView(DeleteView):
    template_name = 'note_delete_form.html'
    queryset = Note.objects.all()
    success_url = '/main/'


# выводит страницу с задачами на конкретную дату
class DateList(ListView):
    model = Note
    template_name = 'date_notes.html'

    # выводит 3 отдельных qs для задач с разным приоритетом + достает текущую дату из урла
    def get_context_data(self, **kwargs):
        context = super(DateList, self).get_context_data(**kwargs)
        context['notes_low'] = Note.objects.filter(note_time=self.kwargs['date']).filter(note_priority=0)
        context['notes_normal'] = Note.objects.filter(note_time=self.kwargs['date']).filter(note_priority=1)
        context['notes_high'] = Note.objects.filter(note_time=self.kwargs['date']).filter(note_priority=2)
        context['date'] = self.kwargs['date']
        return context

