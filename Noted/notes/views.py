from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Tag
from .forms import NoteForm
import datetime


# выводит главную страницу с задачами на текущую неделю
class NotesList(ListView):
    model = Note
    template_name = 'main.html'

    # получает 7 qs по дням недели с датами
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        date = datetime.date.today()
        mon = date - datetime.timedelta(date.weekday())
        week_notes = []
        dates = []
        for i in range(7):
            date = mon + datetime.timedelta(i)
            notes = Note.objects.filter(note_time=date)
            week_notes.append(notes)
            dates.append(date)
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        context['week_notes'] = zip(days, dates, week_notes)
        return context


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

