# Generated by Django 2.2.2 on 2020-07-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuetAns',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q_text', models.CharField(max_length=100)),
                ('Q_img', models.ImageField(upload_to='')),
                ('Q_tag', models.CharField(max_length=100)),
            ],
        ),
    ]