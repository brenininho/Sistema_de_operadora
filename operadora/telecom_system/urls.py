from django.urls import path
from . import views


app_name = 'telecom_system'
urlpatterns = [
    path('clientes', views.index, name='index'),
    path('cliente/<int:pk>', views.client, name='client'),
    path('novo', views.client, name='new_client'),
    path('cliente/<int:pk>/delete', views.delete_client, name='delete_client'),
    path('cliente/<int:pk>/delete_plan', views.delete_plan, name='delete_plan'),
    path('cliente/<int:pk>/adicionar_plano', views.add_plan, name='add_plan'),
]
