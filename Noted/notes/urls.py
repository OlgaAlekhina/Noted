from django.urls import path, register_converter
from .views import main_page, main_page_date, all_notes, note_details, note_edit, all_tasks, \
    task_done, trash, task_delete, note_delete, user_settings, change_password, search, note_perm_delete, \
    task_perm_delete, task_undone, tasks, note_pin, note_unpin
from .path_converters import DateConverter


register_converter(DateConverter, 'date')


urlpatterns = [
    path('', main_page, name='main'),
    path('<date:date>/', main_page_date, name='date_notes'),
    path('notes', all_notes, name='notes'),
    path('notes/<int:pk>', note_details, name='note_details'),
    path('notes/edit/<int:pk>', note_edit, name='note_edit'),
    path('<date:date>/pin/<int:pk>', note_pin, name='note_pin'),
    path('<date:date>/unpin/<int:pk>', note_unpin, name='note_unpin'),
    path('tasks', tasks, name='tasks'),
    path('tasks/<date:date>/', all_tasks, name='tasks_date'),
    path('tasks/<date:date>/edit/<int:pk>', all_tasks, name='task_edit'),
    path('done/<int:pk>', task_done, name='task_done'),
    path('undone/<int:pk>', task_undone, name='task_undone'),
    path('task_delete/<int:pk>', task_delete, name='task_delete'),
    path('note_delete/<int:pk>', note_delete, name='note_delete'),
    path('note_perm_delete/<int:pk>', note_perm_delete, name='note_perm_delete'),
    path('task_perm_delete/<int:pk>', task_perm_delete, name='task_perm_delete'),
    path('trash', trash, name='trash'),
    path('settings', user_settings, name='user_settings'),
    path('settings/change_password', change_password, name='change_password'),
    path('search', search, name='search'),
    ]