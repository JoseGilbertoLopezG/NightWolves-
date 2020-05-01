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
    path('orders', views.AllOrders.as_view(), name='orders'),
    path('order/<int:pk>/status', views.AllStatus.as_view(), name='status'),
    path('order/<int:pk>/received', views.ChangeStatusToReceived.as_view(), name='received'),
    path('order/<int:pk>/prepared', views.ChangeStatusToPrepared.as_view(), name='prepared'),
    path('order/<int:pk>/wait', views.ChangeStatusToWait.as_view(), name='wait'),
    path('order/<int:pk>/onWay', views.ChangeStatusToOnWay.as_view(), name='onWay'),
    path('order/<int:pk>/delivered', views.ChangeStatusToDelivered.as_view(), name='delivered'),
    path('order/<int:pk>/finalized', views.ChangeStatusToFinalized.as_view(), name='finalized'),
    path('order/<int:pk>/canceled', views.ChangeStatusToCanceled.as_view(), name='canceled'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)