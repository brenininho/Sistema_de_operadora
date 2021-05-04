from django.forms import ModelForm
from .models import Client, ChoosePlan


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = '__all__'


class ChoosePlanForm(ModelForm):
    class Meta:
        model = ChoosePlan
        fields = '__all__'
        exclude = ('client',)
