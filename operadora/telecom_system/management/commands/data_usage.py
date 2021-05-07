from django.core.management.base import BaseCommand, CommandError
import random
from telecom_system.models import DataUsage


class Command(BaseCommand):
    help = 'Client usage'

    def handle(self, *args, **kwargs):
        info = random.randint(0, 50)
        info = DataUsage(data_usage=info, client_id=28)
        info.save()
