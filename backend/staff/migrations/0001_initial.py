# Generated by Django 4.2 on 2023-04-28 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('phone_number', models.CharField(max_length=15)),
                ('role', models.CharField(choices=[('administrator', 'Administrator'), ('local', 'Local Teacher'), ('international', 'International Teacher'), ('mentor', 'Mentor'), ('technical', 'Technical Staff')], default='local', max_length=20)),
                ('desc', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images/staff')),
            ],
        ),
    ]
