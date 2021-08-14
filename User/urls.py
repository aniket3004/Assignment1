from django.urls import path
from User import views
from .forms import LoginForm,PostForm
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name='User/login.html',authentication_form=LoginForm), name='login'),
    path('accounts/profile/',views.PostView.as_view(),name="profile"),
]
