# Generated by Django 3.1.1 on 2020-12-09 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto', models.CharField(max_length=300)),
                ('descripcion', models.CharField(max_length=300)),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='FlujoTarea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.empleado')),
            ],
        ),
    ]
