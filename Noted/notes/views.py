from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Tag, Task
from .forms import NoteForm
import datetime


# выводит главную страницу со всеми заметками и задачами на текущую дату
def main_page(request):
    today = datetime.date.today()
    today_tasks = Task.objects.filter(task_time=today)
    notes = Note.objects.all().order_by('-note_time')
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    today = f'{today.day} {month_list[int(today.month) - 1]}'
    return render(request, 'main2.html', context={'today_tasks': today_tasks, 'notes': notes, 'date': today})


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
        context['next_mon'] = mon + datetime.timedelta(7)
        context['prev_mon'] = mon - datetime.timedelta(7)
        context['main'] = True
        return context


# выводит страницу с задачами на следующую неделю
class NextList(ListView):
    model = Note
    template_name = 'main.html'

    # получает 7 qs по дням недели с датами
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mon = self.kwargs['next_mon']
        week_notes = []
        dates = []
        for i in range(7):
            date = mon + datetime.timedelta(i)
            notes = Note.objects.filter(note_time=date)
            week_notes.append(notes)
            dates.append(date)
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        context['week_notes'] = zip(days, dates, week_notes)
        context['next_mon'] = mon + datetime.timedelta(7)
        context['prev_mon'] = mon - datetime.timedelta(7)
        return context


# выводит страницу с задачами на предыдующую неделю
class PrevList(ListView):
    model = Note
    template_name = 'main.html'

    # получает 7 qs по дням недели с датами
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mon = self.kwargs['prev_mon']
        week_notes = []
        dates = []
        for i in range(7):
            date = mon + datetime.timedelta(i)
            notes = Note.objects.filter(note_time=date)
            week_notes.append(notes)
            dates.append(date)
        days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        context['week_notes'] = zip(days, dates, week_notes)
        context['next_mon'] = mon + datetime.timedelta(7)
        context['prev_mon'] = mon - datetime.timedelta(7)
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

