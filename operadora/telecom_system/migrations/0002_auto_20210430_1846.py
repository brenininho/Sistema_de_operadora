# Generated by Django 3.2 on 2021-04-30 18:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telecom_system', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cellphoneplan',
            name='client',
        ),
        migrations.CreateModel(
            name='ChoosePlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plans', models.CharField(choices=[('Starter', 'Starter'), ('Medium', 'Medium'), ('Plus', 'Plus'), ('Premium', 'Premium')], max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='telecom_system.client')),
            ],
        ),
    ]
