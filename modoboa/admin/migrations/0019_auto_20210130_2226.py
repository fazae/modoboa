# Generated by Django 2.2.17 on 2021-01-30 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0018_update_disabled_accounts_aliases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='domain',
            name='name',
            field=models.CharField(help_text='The domain name', max_length=253, unique=True, verbose_name='name'),
        ),
    ]