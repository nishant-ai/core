# Generated by Django 3.2.5 on 2021-07-29 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_alter_quesmcq_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuesIntType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('answer', models.DecimalField(decimal_places=3, max_digits=10)),
                ('correct_answer', models.DecimalField(decimal_places=3, max_digits=10)),
                ('subject', models.CharField(choices=[('PHY', 'Physics'), ('MTH', 'Maths'), ('CHEM', 'Chemistry')], max_length=50)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('publish', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='quesmcq',
            name='answer',
            field=models.CharField(choices=[('option_1', 'Option 1'), ('option_2', 'Option 2'), ('option_3', 'Option 3'), ('option_4', 'Option 4')], max_length=50),
        ),
        migrations.AlterField(
            model_name='quesmcq',
            name='subject',
            field=models.CharField(choices=[('PHY', 'Physics'), ('MTH', 'Maths'), ('CHEM', 'Chemistry')], max_length=50),
        ),
    ]