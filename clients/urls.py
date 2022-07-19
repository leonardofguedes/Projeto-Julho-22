from django.urls import path
from .views.dashboard import *
from .views.all import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('register/create/', register_create, name='create'),
    path('login/', login_view, name='login'),
    path('login/create/', login_create, name='login_create'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', Dashboard, name='dashboard'),
    path('dashboard/animal/<int:id>/edit/',
         dashboard_edit,
         name='dashboard_edit'
         ),
]