# Generated by Django 5.1.2 on 2024-11-27 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cankiet', '0012_alter_items_i_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Rejected', 'rejected'), ('In Progress', 'in-progress'), ('Compeleted', 'completed')], default='I', max_length=11),
        ),
    ]
