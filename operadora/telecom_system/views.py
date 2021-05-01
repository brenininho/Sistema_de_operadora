from django.views import generic
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db import connection
from .models import Client, CellphonePlan, ChoosePlan
from .forms import ClientForm, CellphonePlanForm, ChoosePlanForm


def home(request):
    return render(request, "telecom_system/home.html")


def client(request, pk=None):
    client = None
    if pk is not None:
        client = get_object_or_404(Client, pk=pk)
        form_client = ClientForm(instance=client)
    else:
        form_client = ClientForm()

    form_plan = ChoosePlanForm()
    form_cellphoneplan = CellphonePlanForm()

    if request.method == 'POST':
        if request.POST['form'] == "client":

            if client:
                form_client = ClientForm(request.POST, instance=client)
            else:
                form_client = ClientForm(request.POST)

            if form_client.is_valid():
                client = form_client.save()
                return redirect('telecom_system:client', pk=client.id)

        if request.POST['form'] == "chooseplan":
            form_plan = ChoosePlanForm(request.POST)
            form_plan.instance.client = client
            if form_plan.is_valid():
                form_plan.save()

        if request.POST['form'] == "cellphoneplan":
            form_cellphoneplan = CellphonePlanForm(request.POST)
            form_cellphoneplan.instance.client = client
            if form_cellphoneplan.is_valid():
                form_cellphoneplan.save()

    context = {
        'client': client,
        'form_client': form_client,
        'form_plan': form_plan,
        'form_cellphoneplan': form_cellphoneplan,
    }

    return render(request, 'telecom_system/client.html', context)


def index(request):
    clients = Client.objects.all()
    cellphone_plans = CellphonePlan.objects.all()
    context = {'clients': clients,
               'cellphone_plans': cellphone_plans,
               }
    return render(request, 'telecom_system/index.html', context)


def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('telecom_system:index')


def delete_plan(request, pk):
    plan = get_object_or_404(Client, pk=pk)
    plan.delete()
    return redirect('telecom_system:client', pk=plan.client.id)
