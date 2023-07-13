# Generated by Django 4.2.1 on 2023-06-25 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.FloatField(verbose_name='номер версии')),
                ('version_name', models.CharField(max_length=150, verbose_name='название версии')),
                ('is_active', models.BooleanField(default=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalog.product')),
            ],
            options={
                'verbose_name': 'Версия',
                'verbose_name_plural': 'Версии',
            },
        ),
    ]