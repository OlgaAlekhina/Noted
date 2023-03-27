from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Note, Task
from .forms import TaskForm, UpdateUserForm, UpdateProfileForm
import datetime
import calendar
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.db.models import Q


# выводит главную страницу со всеми заметками и задачами на текущую дату
@login_required
def main_page(request):
    user = request.user
    today = datetime.date.today()
    next_date = today + datetime.timedelta(days=1)
    tasks_active = Task.objects.filter(task_time=today, task_author=user, task_deleted=False, task_priority=False, task_trash=False)
    tasks_deleted = Task.objects.filter(task_time=today, task_author=user, task_deleted=True, task_trash=False)
    tasks_important = Task.objects.filter(task_time=today, task_author=user, task_deleted=False, task_priority=True, task_trash=False)
    notes = Note.objects.filter(note_author=user, note_trash=False).order_by('-note_time')
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    today = f'{today.day} {month_list[int(today.month) - 1]}'
    return render(request, 'main2.html', context={'today_tasks': tasks_active, 'tasks_deleted': tasks_deleted,
                                                  'tasks_important': tasks_important, 'notes': notes, 'date': today,
                                                  'next_date': next_date})


# выводит главную страницу со всеми заметками и задачами на конкретную дату
@login_required
def main_page_date(request, date):
    user = request.user
    next_date = date + datetime.timedelta(days=1)
    tasks_active = Task.objects.filter(task_time=date, task_author=user, task_deleted=False, task_priority=False, task_trash=False)
    tasks_deleted = Task.objects.filter(task_time=date, task_author=user, task_deleted=True, task_trash=False)
    tasks_important = Task.objects.filter(task_time=date, task_author=user, task_deleted=False, task_priority=True, task_trash=False)
    notes = Note.objects.filter(note_author=user, note_trash=False).order_by('-note_time')
    month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
                  'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
    date = f'{date.day} {month_list[int(date.month) - 1]}'
    return render(request, 'main2.html', context={'today_tasks': tasks_active, 'tasks_deleted': tasks_deleted,
                                                  'tasks_important': tasks_important, 'notes': notes, 'date': date,
                                                  'next_date': next_date})


# выводит страницу со всеми существующими заметками и формой добавления новой
@login_required
def all_notes(request):
    user = request.user
    if request.method == "POST":
        note_title = request.POST['note_title']
        note_text = request.POST['note_text']
        note_time = datetime.date.today()
        Note.objects.create(note_title=note_title, note_text=note_text, note_author=user, note_time=note_time)
        return redirect('notes')
    else:
        notes = Note.objects.filter(note_author=user, note_trash=False).order_by('-note_time')
        return render(request, 'notes.html', context={'notes': notes})


# выводит страницу со всеми существующими заметками и одной конкретной заметкой в полноэкранном режиме
@login_required
def note_details(request, pk):
    user = request.user
    notes = Note.objects.filter(note_author=user, note_trash=False).order_by('-note_time')
    note = Note.objects.get(id=pk)
    return render(request, 'note_details.html', context={'notes': notes, 'note': note})


# выводит страницу со всеми существующими заметками и формой редактирования одной конкретной заметки
@login_required
def note_edit(request, pk):
    user = request.user
    if request.method == "POST":
        note_title = request.POST['note_title']
        note_text = request.POST['note_text']
        note_time = datetime.date.today()
        Note.objects.filter(id=pk).update(note_title=note_title, note_text=note_text, note_time=note_time)
        return redirect('notes')
    else:
        note = Note.objects.get(id=pk)
        notes = Note.objects.filter(note_author=user, note_trash=False).order_by('-note_time')
        return render(request, 'note_edit.html', context={'notes': notes, 'note': note})


# выводит страницу с задачами на текущую дату и формой добавления новой либо формой редактирования старой
@login_required
def all_tasks(request, pk=None):
    user = request.user
    today = datetime.date.today()
    tasks_active = Task.objects.filter(task_time=today, task_author=user, task_deleted=False, task_priority=False, task_trash=False)
    tasks_deleted = Task.objects.filter(task_time=today, task_author=user, task_deleted=True, task_trash=False)
    tasks_important = Task.objects.filter(task_time=today, task_author=user, task_deleted=False, task_priority=True, task_trash=False)

    try:
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)
    except:
        form = TaskForm()

    if request.method == "POST":
        task_title = request.POST['task_title']
        task_time = request.POST['task_time']
        task_priority = request.POST.get('task_priority', False)
        if task_priority == 'on':
            task_priority = True
        try:
            print('start')
            task = Task.objects.get(id=pk)
            Task.objects.filter(id=pk).update(task_title=task_title, task_priority=task_priority, task_time=task_time)
            print('end')
        except:
            print('start2')
            Task.objects.create(task_title=task_title, task_priority=task_priority, task_author=user, task_time=task_time)
            print('end2')
        return redirect('tasks')

    return render(request, 'tasks.html', context={'today_tasks': tasks_active, 'tasks_deleted': tasks_deleted,
                                                      'tasks_important': tasks_important, 'form': form})


# функция для зачеркивания задачи при нажатии на кружок
@login_required
def task_done(request, pk):
    Task.objects.filter(id=pk).update(task_deleted=True)
    next = request.GET.get('next', reverse('main'))
    return HttpResponseRedirect(next)


# выводит корзину с удаленными задачами и заметками
@login_required
def trash(request):
    user = request.user
    task_trash = Task.objects.filter(task_author=user, task_trash=True)
    note_trash = Note.objects.filter(note_author=user, note_trash=True)
    return render(request, 'trash.html', context={'task_trash': task_trash, 'note_trash': note_trash})


# функция для удаления задачи в корзину при нажатии на иконку мусорной корзины
@login_required
def task_delete(request, pk):
    Task.objects.filter(id=pk).update(task_trash=True)
    next = request.GET.get('next', reverse('main'))
    return HttpResponseRedirect(next)


# функция для удаления заметки в корзину при нажатии на иконку мусорной корзины
@login_required
def note_delete(request, pk):
    Note.objects.filter(id=pk).update(note_trash=True)
    next = request.GET.get('next', reverse('notes'))
    return HttpResponseRedirect(next)


# функция для удаления задачи из корзины и из базы данных
@login_required
def task_perm_delete(request, pk):
    Task.objects.filter(id=pk).delete()
    return redirect('trash')


# функция для удаления заметки из корзины и из базы данных
@login_required
def note_perm_delete(request, pk):
    Note.objects.filter(id=pk).delete()
    return redirect('trash')


# выводит страницу настроек данных пользователя
@login_required
def user_settings(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Ваш профиль успешно обновлен')
            return redirect('user_settings')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.userprofile)

    return render(request, 'settings.html', {'user_form': user_form, 'profile_form': profile_form})


# выводит страницу настроек данных пользователя с формой смены пароля
@login_required
def change_password(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if user_form.is_valid() and profile_form.is_valid():
            if password1 and password2 and password1 != password2:
                messages.error(request, "Пароли не совпадают.")
            else:
                request.user.set_password(password1)
                request.user.save()
                user_form.save()
                profile_form.save()
                login(request, request.user)
                messages.success(request, 'Ваш профиль успешно обновлен')
                return redirect('user_settings')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.userprofile)

    return render(request, 'change_password.html', {'user_form': user_form, 'profile_form': profile_form})


# выводит страницу с результатами поиска
@login_required
def search(request):
    user = request.user
    q = request.GET.get("q")
    note_search = Note.objects.filter(note_author=user, note_title__contains=q)
    task_search_imp = Task.objects.filter(task_title__contains=q).filter(task_author=user, task_deleted=False, task_priority=True, task_trash=False)
    task_search = Task.objects.filter(task_title__contains=q).filter(task_author=user, task_deleted=False, task_priority=False, task_trash=False)
    task_search_done = Task.objects.filter(task_title__contains=q).filter(task_author=user, task_deleted=True, task_trash=False)
    return render(request, 'search.html', context={'note_search': note_search, 'task_search': task_search,
                                                   'task_search_imp': task_search_imp,
                                                   'task_search_done': task_search_done})





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