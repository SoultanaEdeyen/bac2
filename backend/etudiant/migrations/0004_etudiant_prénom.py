# Generated by Django 4.1.7 on 2023-04-18 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('etudiant', '0003_delete_adm'),
    ]

    operations = [
        migrations.AddField(
            model_name='etudiant',
            name='prénom',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
