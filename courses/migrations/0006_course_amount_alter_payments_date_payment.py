# Generated by Django 4.2.6 on 2023-12-05 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_alter_course_owner_alter_lesson_owner_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='amount',
            field=models.IntegerField(default=10000, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='payments',
            name='date_payment',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Дата оплаты'),
        ),
    ]
