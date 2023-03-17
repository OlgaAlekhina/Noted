from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Task
from .forms import TaskForm
import datetime
import calendar
from django.http import HttpResponseRedirect
from django.urls import reverse


# выводит главную страницу со всеми заметками и задачами на текущую дату
def main_page(request):
    today = datetime.date.today()
    next_date = today + datetime.timedelta(days=1)
    tasks_active = Task.objects.filter(task_time=today, task_deleted=False, task_priority=False)
    tasks_deleted = Task.objects.filter(task_time=today, task_deleted=True)
    tasks_important = Task.objects.filter(task_time=today, task_deleted=False, task_priority=True)
    notes = Note.objects.all().order_by('-note_time')
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    today = f'{today.day} {month_list[int(today.month) - 1]}'
    return render(request, 'main2.html', context={'today_tasks': tasks_active, 'tasks_deleted': tasks_deleted,
                                                  'tasks_important': tasks_important, 'notes': notes, 'date': today,
                                                  'next_date': next_date})


# выводит главную страницу со всеми заметками и задачами на конкретную дату
def main_page_date(request, date):
    next_date = date + datetime.timedelta(days=1)
    tasks_active = Task.objects.filter(task_time=date, task_deleted=False, task_priority=False)
    tasks_deleted = Task.objects.filter(task_time=date, task_deleted=True)
    tasks_important = Task.objects.filter(task_time=date, task_deleted=False, task_priority=True)
    notes = Note.objects.all().order_by('-note_time')
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date = f'{date.day} {month_list[int(date.month) - 1]}'
    return render(request, 'main2.html', context={'today_tasks': tasks_active, 'tasks_deleted': tasks_deleted,
                                                  'tasks_important': tasks_important, 'notes': notes, 'date': date,
                                                  'next_date': next_date})


# выводит страницу со всеми существующими заметками и формой добавления новой
def all_notes(request):
    if request.method == "POST":
        note_title = request.POST['note_title']
        note_text = request.POST['note_text']
        note_author = request.user
        note_time = datetime.date.today()
        Note.objects.create(note_title=note_title, note_text=note_text, note_author=note_author, note_time=note_time)
        return redirect('notes')
    else:
        notes = Note.objects.all().order_by('-note_time')
        return render(request, 'notes.html', context={'notes': notes})


# выводит страницу со всеми существующими заметками и одной конкретной заметкой в полноэкранном режиме
def note_details(request, pk):
    notes = Note.objects.all().order_by('-note_time')
    note = Note.objects.get(id=pk)
    return render(request, 'note_details.html', context={'notes': notes, 'note': note})


# выводит страницу со всеми существующими заметками и формой редактирования одной конкретной заметки
def note_edit(request, pk):
    if request.method == "POST":
        note_title = request.POST['note_title']
        note_text = request.POST['note_text']
        note_time = datetime.date.today()
        Note.objects.filter(id=pk).update(note_title=note_title, note_text=note_text, note_time=note_time)
        return redirect('notes')
    else:
        note = Note.objects.get(id=pk)
        notes = Note.objects.all().order_by('-note_time')
        return render(request, 'note_edit.html', context={'notes': notes, 'note': note})


# выводит страницу с задачами на текущую дату и формой добавления новой
def all_tasks(request):
    if request.method == "POST":
        task_title = request.POST['task_title']
        task_author = request.user
        task_time = request.POST['task_time']
        task_priority = request.POST.get('task_priority', False)
        if task_priority == 'on':
            task_priority = True
        Task.objects.create(task_title=task_title, task_priority=task_priority, task_author=task_author, task_time=task_time)
        return redirect('tasks')
    else:
        today = datetime.date.today()
        tasks_active = Task.objects.filter(task_time=today, task_deleted=False, task_priority=False)
        tasks_deleted = Task.objects.filter(task_time=today, task_deleted=True)
        tasks_important = Task.objects.filter(task_time=today, task_deleted=False, task_priority=True)
        form = TaskForm()
        return render(request, 'tasks.html', context={'today_tasks': tasks_active, 'tasks_deleted': tasks_deleted,
                                                      'tasks_important': tasks_important, 'form': form})


# функция для зачеркивания задачи при нажатии на иконку мусорной корзинки
def task_done(request, pk):
    Task.objects.filter(id=pk).update(task_deleted=True)
    next = request.GET.get('next', reverse('main'))
    return HttpResponseRedirect(next)





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
# class NoteAddView(CreateView):
#     template_name = 'note_add_form.html'
#     form_class = NoteForm
#
#     # это чтобы автором задачи автоматически считался текущий юзер
#     def get_initial(self):
#         initial = super().get_initial()
#         initial['note_author'] = self.request.user
#         return initial


# выводит форму для редактирования задачи
# class NoteUpdateView(UpdateView):
#     template_name = 'note_update_form.html'
#     form_class = NoteForm
#
#     def get_object(self, **kwargs):
#         id = self.kwargs.get('pk')
#         return Note.objects.get(pk=id)


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


# вывод календаря на питоне, но он не может переключать месяцы без перезагрузки страницы, поэтому сделала другой вариант календаря на Javascript
noted_calendar = calendar.Calendar()
def calendar(request):
    today = datetime.date.today()  # получаем текущую дату (можем использовать из нее today.day, today.month, today.year)

    list_weeks = noted_calendar.monthdatescalendar(today.year, today.month) # список списков (по неделям) с датами в формате datetime.date objects

    return render(request, 'calendar.html', context={'list_weeks': list_weeks, 'today': today})