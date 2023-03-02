from django.urls import path, register_converter
from .views import main_page, NoteDetail, calendar, DateList, NoteAddView, NoteUpdateView, NoteDeleteView, NextList, PrevList
from .path_converters import DateConverter


register_converter(DateConverter, 'date')


urlpatterns = [
    path('', main_page, name='main'),
    path('<int:pk>', NoteDetail.as_view(), name='note_detail'),
    path('add', NoteAddView.as_view(), name='note_add'),
    path('edit/<int:pk>', NoteUpdateView.as_view(), name='note_edit'),
    path('delete/<int:pk>', NoteDeleteView.as_view(), name='note_delete'),
    path('<date:date>/', DateList.as_view(), name='date_notes'),
    path('next/<date:next_mon>/', NextList.as_view(), name='next_notes'),
    path('previous/<date:prev_mon>/', PrevList.as_view(), name='previous_notes'),
    path('cal', calendar, name='calendar'),

    ]