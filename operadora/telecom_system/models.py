from django.contrib import admin
from django.db import models


class Client(models.Model):
    def __str__(self):
        return f"{self.name}, {self.cpf}, {self.gender}"

    name = models.CharField("Nome", max_length=100, null=False)
    cpf = models.CharField(max_length=11, null=False)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=30, choices=[
        ("Masculino", "Masculino"),
        ("Feminino", "Feminino"),
        ("outros", "outros"),
    ])


class ChoosePlan(models.Model):
    def __str__(self):
        return f'{self.plans}'

    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    plans = models.CharField(max_length=50, choices=[
        ("Starter", "Starter"),
        ("Medium", "Medium"),
        ("Plus", "Plus"),
        ("Premium", "Premium"),
    ])
