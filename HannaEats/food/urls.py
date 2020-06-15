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
    path('orders/<int:pk>', views.AllOrders.as_view(), name='orders'),
    path('orders/history', views.HistoryOrders.as_view(), name='history'),
    path('category/all', views.CategoriaVista.as_view(), name='category_view'),
    path('category/<str:name>', views.ComidaVista.as_view(), name='food_view'),
    # Views para Categorias
    path('category', views.AllCategorys.as_view(), name='category'),
    path('category/add/category', views.AddCategory.as_view(), name='add_categ'),
    path('category/<int:pk>/del_categ', views.DelCategory.as_view(), name='del_categ'),
    path('category/<int:pk>/updt_categ', views.UpdateCategory.as_view(), name='updt_categ'),
    # Views para Alimentos
    path('all', views.AllFood.as_view(), name='foods'),
    # Views de gestion de alimentos
    path('add_food', views.AddFood.as_view(), name='add_food'),
    path('<int:pk>/del_food', views.DelFood.as_view(), name='del_food'),
    path('<int:pk>/updt_food', views.UpdateFood.as_view(), name='updt_food'),
    # Views de Cambio de estado de orden
    path('order/<int:pk>/status', views.AllStatus.as_view(), name='status'),
    path('order/<int:pk>/received', views.ChangeStatusToReceived.as_view(), name='received'),
    path('order/<int:pk>/prepared', views.ChangeStatusToPrepared.as_view(), name='prepared'),
    path('order/<int:pk>/onWay', views.ChangeStatusToOnWay.as_view(), name='onWay'),
    path('order/<int:pk>/finalized', views.ChangeStatusToFinalized.as_view(), name='finalized'),
    path('order/<int:pk>/canceled', views.ChangeStatusToCanceled.as_view(), name='canceled'),
    path('order/<int:pk>/ready', views.ChangeStatusToReady.as_view(), name='ready'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
