from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Client, ChoosePlan
from .forms import ClientForm, ChoosePlanForm


def home(request):
    return render(request, "telecom_system/home.html")


def add_plan(request, pk):
    form_plan = ChoosePlanForm()
    client = get_object_or_404(Client, pk=pk)
    if request.method == 'POST':
        form_plan = ChoosePlanForm(request.POST)
        form_plan.instance.client = client
        if form_plan.is_valid():
            form_plan.save()
            return redirect('telecom_system:index')
    context = {
        'form_plan': form_plan,
        'client': client,
    }
    return render(request, 'telecom_system/add_plan.html', context)


def client(request, pk=None):
    if pk is not None:
        client = get_object_or_404(Client, pk=pk)
        form_client = ClientForm(instance=client)
    else:
        form_client = ClientForm()
        client = None

    if request.method == 'POST':

        if client:
            form_client = ClientForm(request.POST, instance=client)
        else:
            form_client = ClientForm(request.POST)

        if form_client.is_valid():
            form_client.save()
            return redirect('telecom_system:index')
    context = {
        'form_client': form_client,
        'client': client,
    }
    return render(request, 'telecom_system/client.html', context)


def index(request):
    clients = Client.objects.all()
    context = {'clients': clients
               }
    return render(request, 'telecom_system/index.html', context)


def delete_client(request, pk):
    client = get_object_or_404(Client, pk=pk)
    client.delete()
    return redirect('telecom_system:index')


def delete_plan(request, pk):
    plan = get_object_or_404(ChoosePlan, pk=pk)
    plan.delete()
    return redirect('telecom_system:client', pk=plan.client.id)
