from django.urls import path
from .views import register_request
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('signin/', register_request, name='signin'),
    path('login/', LoginView.as_view(template_name ='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    # path('confirmation/<int:user_id>/', verify_registration, name='confirmation'),
    ]