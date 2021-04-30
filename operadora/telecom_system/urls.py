from django.urls import path
from . import views

app_name = 'telecom_system'
urlpatterns = [
    path('', views.client, name='client'),
    path('<int:pk>/', views.client_query, name='client_query'),
]
