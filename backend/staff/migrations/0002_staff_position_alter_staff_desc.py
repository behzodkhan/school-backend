# Generated by Django 4.2 on 2023-04-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='position',
            field=models.CharField(default='Kulgu', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='staff',
            name='desc',
            field=models.TextField(),
        ),
    ]
