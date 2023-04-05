from django.urls import path
from .views import register_request, login_user, reset_password_request, password_reset_confirm
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('signup/', register_request, name='signup'),
    path('login/', login_user, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('reset_password/', reset_password_request, name='reset_password'),
    path('reset/<uidb64>/<token>', password_reset_confirm, name='password_reset_confirm'),
    ]