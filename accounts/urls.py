from django.urls import path,include
from .forms import HotelLoginForm
from  django.contrib.auth.views import LoginView
from . import views


app_name = 'accounts'



urlpatterns = [
    path('login/',LoginView.as_view(form_class=HotelLoginForm, template_name='registration/login.html'),name='login'),
    path('',include('django.contrib.auth.urls')),
    path('register/',views.register,name='register'),
    path('new_user/',views.new_register_view,name='new_user'),
    path('user_confirm/<int:user_id>/',views.user_confirm,name='user_confirm'),
    path('confirmed_users/',views.confirmed_users,name='confirmed_users')
]