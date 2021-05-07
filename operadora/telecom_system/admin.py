from django.contrib import admin
from .models import Client, ChoosePlan, DataUsage


class ChoosePlansInline(admin.TabularInline):
    model = ChoosePlan
    extra = 1


class DataUsageInline(admin.TabularInline):
    model = DataUsage
    extra = 1


class ClientAdmin(admin.ModelAdmin):
    fields = ['name', 'cpf', 'birth_date', 'gender']
    inlines = [ChoosePlansInline, DataUsageInline]
    list_display = ("name", "cpf", "birth_date", "gender")
    list_filter = ["birth_date"]
    search_fields = ["name"]


admin.site.register(Client, ClientAdmin)
