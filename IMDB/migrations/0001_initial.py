# Generated by Django 4.2.4 on 2023-09-02 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filme', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('nota', models.DecimalField(decimal_places=1, max_digits=2)),
                ('filme', models.ForeignKey(max_length=100, null=True, on_delete=django.db.models.deletion.CASCADE, to='IMDB.filme')),
            ],
        ),
    ]
