# Generated by Django 4.0.4 on 2022-10-24 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contribution', '0003_alter_contribution_date_received'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contribution',
            old_name='type',
            new_name='contribution_type',
        ),
    ]