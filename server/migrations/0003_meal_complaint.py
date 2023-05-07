# Generated by Django 4.1.3 on 2023-04-17 20:36

from django.db import migrations, models
import django.db.models.deletion
import server.models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_techinventory_type_alter_cultinventory_quantity_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('S', 'Snacks'), ('D', 'Dinner')], max_length=5)),
                ('weight', models.CharField(blank=True, max_length=6, null=True)),
                ('date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='server.student')),
            ],
            options={
                'ordering': ['-date', 'student__rollNumber'],
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('type', models.CharField(choices=[('mess', 'Mess'), ('maint', 'Maintanence')], default='maint', max_length=20)),
                ('date', models.DateField(auto_now_add=True)),
                ('image', models.ImageField(upload_to=server.models.complaint_handler)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='server.student')),
            ],
        ),
    ]
