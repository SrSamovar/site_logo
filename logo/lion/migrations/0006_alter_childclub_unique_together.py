# Generated by Django 4.2.14 on 2024-10-03 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lion', '0005_childclub_teacher'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='childclub',
            unique_together={('child', 'club', 'teacher')},
        ),
    ]
