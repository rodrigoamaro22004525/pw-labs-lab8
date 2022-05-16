# Generated by Django 4.0.4 on 2022-05-16 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('prioridade', models.IntegerField(default=1)),
                ('concluido', models.BooleanField(default=False)),
                ('criado', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
