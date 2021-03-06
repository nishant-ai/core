# Generated by Django 3.2.5 on 2021-07-30 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0009_auto_20210730_0652'),
    ]

    operations = [
        migrations.AddField(
            model_name='quesinttype',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
        migrations.AddField(
            model_name='quesmcq',
            name='question_image',
            field=models.ImageField(blank=True, null=True, upload_to='media/images'),
        ),
        migrations.AlterField(
            model_name='quesinttype',
            name='question',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='quesmcq',
            name='question',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
