# Generated by Django 2.0.2 on 2018-08-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='C:\\Users\\Kiran\\Desktop\\Coding\\Python\\RobinhoodArmy', width_field='width_field')),
                ('height_field', models.IntegerField(default=300)),
                ('width_field', models.IntegerField(default=600)),
            ],
        ),
    ]