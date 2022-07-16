from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('pet/', one_only_view, name='one-only'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)