# Generated by Django 3.2.6 on 2022-09-18 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Models', '0008_alter_ticket_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='ticket',
            unique_together={('receiver', 'title')},
        ),
    ]
