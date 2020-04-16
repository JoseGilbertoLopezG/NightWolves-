# Django
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# Views
from users import views

app_name = "users"

urlpatterns = [
    path('add-directions', views.AddDir.as_view(), name='add-directions'),
    path('all-directions', views.AllDir.as_view(), name='all-directions'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)