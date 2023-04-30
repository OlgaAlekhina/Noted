from django.shortcuts import render, redirect
from .models import Note, Task
from .forms import TaskForm, UpdateUserForm, UpdateProfileForm
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from django.utils import timezone


# выводит главную страницу со всеми заметками и задачами на текущую дату
@login_required
def main_page(request):
    user = request.user
    today = datetime.datetime.today().astimezone()
    next_date = today + datetime.timedelta(days=1)
    tasks_active = Task.objects.filter(task_date=today, task_author=user, task_deleted=False, task_priority=False,
                                       task_trash=False).order_by('-add_at')
    tasks_deleted = Task.objects.filter(task_date=today, task_author=user, task_deleted=True, task_trash=False).order_by('add_at')
    tasks_important = Task.objects.filter(task_date=today, task_author=user, task_deleted=False, task_priority=True,
                                          task_trash=False).order_by('-add_at')
    notes = Note.objects.filter(note_author=user, note_trash=False).order_by('-add_at')
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
    tasks_active = Task.objects.filter(task_date=date, task_author=user, task_deleted=False, task_priority=False,
                                       task_trash=False).order_by('-add_at')
    tasks_deleted = Task.objects.filter(task_date=date, task_author=user, task_deleted=True, task_trash=False).order_by('add_at')
    tasks_important = Task.objects.filter(task_date=date, task_author=user, task_deleted=False, task_priority=True,
                                          task_trash=False).order_by('-add_at')
    notes = Note.objects.filter(note_author=user, note_trash=False).order_by('-add_at')
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
        add_at = timezone.now()
        try:
            note_file = request.FILES['note_file']
            Note.objects.create(note_title=note_title, note_text=note_text, note_author=user,
                                note_file=note_file, add_at=add_at)
        except:
            Note.objects.create(note_title=note_title, note_text=note_text, note_author=user,
                                add_at=add_at)
        return redirect('notes')
    else:
        notes = Note.objects.filter(note_author=user, note_trash=False).order_by('-add_at')
        return render(request, 'notes.html', context={'notes': notes})


# выводит страницу со всеми существующими заметками и одной конкретной заметкой в полноэкранном режиме
@login_required
def note_details(request, pk):
    user = request.user
    notes = Note.objects.filter(note_author=user, note_trash=False).order_by('-add_at')
    note = Note.objects.get(id=pk)
    return render(request, 'note_details.html', context={'notes': notes, 'note': note})


# выводит страницу со всеми существующими заметками и формой редактирования одной конкретной заметки
@login_required
def note_edit(request, pk):
    user = request.user
    if request.method == "POST":
        note_title = request.POST['note_title']
        note_text = request.POST['note_text']
        file_delete = request.POST.get('file_delete', False)
        add_at = timezone.now()
        if file_delete == 'on':
            Note.objects.filter(id=pk).update(note_file=None, note_trash=False)
        try:
            note_file = request.FILES['note_file']
            note = Note.objects.get(id=pk)
            note.note_file = note_file
            note.note_title = note_title
            note.note_text = note_text
            note.add_at = add_at
            note.save()
        except:
            Note.objects.filter(id=pk).update(note_title=note_title, note_text=note_text, add_at=add_at, note_trash=False)
        return redirect('notes')
    else:
        note = Note.objects.get(id=pk)
        notes = Note.objects.filter(note_author=user, note_trash=False).order_by('-add_at')
        return render(request, 'note_edit.html', context={'notes': notes, 'note': note})


# выводит страницу с задачами на текущую дату и формой добавления новой либо формой редактирования старой
@login_required
def all_tasks(request, pk=None):
    user = request.user
    today = datetime.datetime.today().astimezone()
    tasks_active = Task.objects.filter(task_date=today, task_author=user, task_deleted=False, task_priority=False,
                                       task_trash=False).order_by('-add_at')
    tasks_deleted = Task.objects.filter(task_date=today, task_author=user, task_deleted=True, task_trash=False).order_by('add_at')
    tasks_important = Task.objects.filter(task_date=today, task_author=user, task_deleted=False, task_priority=True,
                                          task_trash=False).order_by('-add_at')
    try:
        task = Task.objects.get(id=pk)
        form = TaskForm(instance=task)
    except:
        form = TaskForm()

    if request.method == "POST":
        task_title = request.POST['task_title']
        task_date = request.POST['task_date']
        task_priority = request.POST.get('task_priority', False)
        add_at = timezone.now()
        if task_priority == 'on':
            task_priority = True
        try:
            task = Task.objects.get(id=pk)
            Task.objects.filter(id=pk).update(task_title=task_title, task_priority=task_priority, task_date=task_date,
                                              add_at=add_at)
        except:
            Task.objects.create(task_title=task_title, task_priority=task_priority, task_author=user,
                                task_date=task_date, add_at=add_at)
        return redirect('tasks')

    return render(request, 'tasks.html', context={'today_tasks': tasks_active, 'tasks_deleted': tasks_deleted,
                                                      'tasks_important': tasks_important, 'form': form, 'task': pk})


# функция для зачеркивания задачи при нажатии на кружок
@login_required
def task_done(request, pk):
    Task.objects.filter(id=pk).update(task_deleted=True)
    next = request.GET.get('next', reverse('main'))
    return HttpResponseRedirect(next)


# функция для восстановления задачи при нажатии на отмеченный кружок
@login_required
def task_undone(request, pk):
    Task.objects.filter(id=pk).update(task_deleted=False)
    next = request.GET.get('next', reverse('main'))
    if next == reverse('search'):
        next = reverse('main')
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
    note_search = Note.objects.filter(note_author=user, note_title__icontains=q).order_by('-add_at')
    task_search_imp = Task.objects.filter(task_title__icontains=q).filter(task_author=user, task_deleted=False,
                                                                         task_priority=True, task_trash=False).order_by('-add_at')
    task_search = Task.objects.filter(task_title__icontains=q).filter(task_author=user, task_deleted=False, task_priority=False, task_trash=False).order_by('-add_at')
    task_search_done = Task.objects.filter(task_title__icontains=q).filter(task_author=user, task_deleted=True,
                                                                          task_trash=False).order_by('add_at')
    return render(request, 'search.html', context={'note_search': note_search, 'task_search': task_search,
                                                   'task_search_imp': task_search_imp,
                                                   'task_search_done': task_search_done})
























