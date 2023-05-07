# Generated by Django 4.1.3 on 2023-05-04 04:58

from django.db import migrations, models
import server.models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0011_hostelconstitution_amended'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to=server.models.otherimages)),
            ],
        ),
    ]
