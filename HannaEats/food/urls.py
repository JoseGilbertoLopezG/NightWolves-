# Django
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# Views
from food import views

app_name = "food"

urlpatterns = [
    path('', views.IndexFood.as_view(), name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)