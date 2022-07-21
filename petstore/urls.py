from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from petstore.views.views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('pet/<int:id>/', one_only_view, name='one-only'),
                  path(
                      'pet/theory/',
                      theory,
                      name='theory',
                  )
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)