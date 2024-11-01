from django.urls import path
from .views import register_view, login_view, user_list_view, home_view

urlpatterns = [
    path('register/', register_view, name = 'register'),
    path('login/', login_view, name = 'login'),
    path('', user_list_view, name='user_list'),
    path('', home_view, name='home'),
]
