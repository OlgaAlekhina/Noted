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
    # path('<int:pk>/reply', ReplyCreateView.as_view(), name='reply'),
    # path('thanks', ThanksView.as_view(), name='thanks'),
    # path('messages/', MessagesView.as_view(), name='messages'),
    # path('messages/<int:pk>/delete/', ReplyDeleteView.as_view(), name='reply_delete'),
    # path('messages/<int:pk>/accept/', accept_reply, name='reply_accept'),
    path('list/<date:date>/', DateList.as_view(), name='date_notes'),

    ]