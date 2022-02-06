# Generated by Django 4.0.2 on 2022-02-05 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investigation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('InvestigationTitle', models.CharField(max_length=200)),
                ('InvestigationFile', models.FileField(upload_to='')),
                ('InvestigationDate', models.DateTimeField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
            ],
        ),
    ]
