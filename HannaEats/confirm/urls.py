# Django
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# Views
from confirm import views

app_name = "confirm"

urlpatterns = [
    path('email/', views.ConfirmEmail.as_view(), name = 'confirm-email'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
