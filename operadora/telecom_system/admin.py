from django.contrib import admin
from .models import Client, CellphonePlan, ChoosePlan


class CellphonePlanAdmin(admin.ModelAdmin):
    fields = ['name', 'price', 'premium_data', 'lines']
    list_display = ("name", "price", "premium_data", "lines")
    list_filter = ["premium_data"]
    search_fields = ["name"]


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
admin.site.register(CellphonePlan, CellphonePlanAdmin)
