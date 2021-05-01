from django.urls import path
from . import views

app_name = 'telecom_system'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.client, name='client'),
    path('novo', views.client, name='new_client'),
    path('<int:pk>/delete_client', views.delete_client, name='delete_client'),
]
