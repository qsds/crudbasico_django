# Generated by Django 2.1.14 on 2019-12-04 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_remove_empleado_sexo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]