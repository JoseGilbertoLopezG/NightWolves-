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
    path('logout', views.Logout.as_view(), name='logout'),
    path('verificar/<str:correo>', views.VerifyCount.as_view(), name='verificar'),
    #Views de carrito de compras
    path('<int:pk>/<int:food>/add-item', views.CartAdd.as_view(), name='add-item'),
    path('<int:pk>/all-items', views.CartAll.as_view(), name='all-item'),
    path('upd-cart/<int:pk>', views.CartUpdate.as_view(), name='upd-item'),
    path('del-item/<int:pk>/', views.CartDel.as_view(), name='del-item'),
    path('cart/checkout', views.CartCheckout.as_view(), name='checkout-cart'),
    #Views de creación de cuentas 
    path("create-client-account", views.CreateClient.as_view(), name='create-client'),
    path("create-delivery-account", views.CreateAccount.as_view(), name='create-account'),
    #Views de gestión de direcciones 
    path('<int:pk>/add-directions', views.AddDir.as_view(), name='add-directions'),
    path('<int:pk>/all-directions', views.AllDir.as_view(), name='all-directions'),
    path('upd-directions/<int:pk>', views.UpdateDir.as_view(), name='upd-directions'),
    path('del-directions/<int:pk>', views.DelDir.as_view(), name='del-directions'),
    # Views de Calificaion de orden
    path('order/<int:pk>/1_star', views.OneStar.as_view(), name='1star'),
    path('order/<int:pk>/2_stars', views.TwoStars.as_view(), name='2star'),
    path('order/<int:pk>/3_stars', views.ThreeStars.as_view(), name='3star'),
    path('order/<int:pk>/4_stars', views.FourStars.as_view(), name='4star'),
    path('order/<int:pk>/5_stars', views.FiveStars.as_view(), name='5star'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
