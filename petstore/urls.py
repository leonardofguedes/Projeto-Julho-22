from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from petstore.views.views import *
from petstore.views.views_form_add_pet import *

urlpatterns = [
    path('', home_view, name='home'),
    path('pet/<int:id>/', one_only_view, name='one-only'),
    path('pet/pet-add/', pet_view, name='pet-register'),
    path('pet/create/', pet_create, name='pet-create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)