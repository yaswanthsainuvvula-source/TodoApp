from django.urls import path
from .views import home,user_registration
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('',home,name='home'),
    path('signup/',user_registration,name='signup'),
    path('login/',LoginView.as_view(template_name='app1/login.html'),name='login')
]
