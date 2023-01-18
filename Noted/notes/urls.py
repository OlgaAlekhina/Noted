from django.urls import path, register_converter
from .views import NoteDetail, NotesList, DateList, NoteAddView, NoteUpdateView, NoteDeleteView
from .path_converters import DateConverter


register_converter(DateConverter, 'date')


urlpatterns = [
    path('', NotesList.as_view(), name='main'),
    path('<int:pk>', NoteDetail.as_view(), name='note_detail'),
    path('add', NoteAddView.as_view(), name='note_add'),
    path('edit/<int:pk>', NoteUpdateView.as_view(), name='note_edit'),
    path('delete/<int:pk>', NoteDeleteView.as_view(), name='note_delete'),
    path('<date:date>/', DateList.as_view(), name='date_notes'),

    ]