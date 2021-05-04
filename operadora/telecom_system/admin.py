from django.contrib import admin
from .models import Client, ChoosePlan


class ChoosePlansInline(admin.TabularInline):
    model = ChoosePlan
    extra = 1


class ClientAdmin(admin.ModelAdmin):
    fields = ['name', 'cpf', 'birth_date', 'gender']
    inlines = [ChoosePlansInline]
    list_display = ("name", "cpf", "birth_date", "gender")
    list_filter = ["birth_date"]
    search_fields = ["name"]


admin.site.register(Client, ClientAdmin)
