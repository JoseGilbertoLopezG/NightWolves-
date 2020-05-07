# Django
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# Views
from users import views

app_name = "users"

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path("create-client-account", views.CreateClient.as_view(), name='create-client'),
    path("create-delivery-account", views.CreateAccount.as_view(), name='create-account'),
    path('add-directions', views.AddDir.as_view(), name='add-directions'),
    path('all-directions', views.AllDir.as_view(), name='all-directions'),
    path('upd-directions/<int:pk>', views.UpdateDir.as_view(), name='upd-directions'),
    path('del-directions/<int:pk>', views.DelDir.as_view(), name='del-directions'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
