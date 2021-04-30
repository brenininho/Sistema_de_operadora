from django.views import generic
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db import connection
from .models import Client, CellphonePlan, ChoosePlan


def client_query(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, "create_client.html", context)


def client(request):
    clients = Client.objects.all()
    context = {'clients': clients}
    return render(request, 'client.html', context)
