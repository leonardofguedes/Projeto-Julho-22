from django.urls import path
from .views.dashboard import *
from .views.all import *

urlpatterns = [
    path('register/', register_view, name='register'),
    path('register/create/', register_create, name='create'),
    path('login/', login_view, name='login'),
    path('login/create/', login_create, name='login_create'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/animal/new/',
         Dashboard.as_view(),
         name='dashboard-animal-new'),
    path('dashboard/animal/delete/',
         Dashboard_Delete.as_view(),
         name='dashboard-animal-delete'),
    path('dashboard/animal/<int:id>/edit/',
         Dashboard.as_view(),
         name='dashboard-edit'
         ),
]