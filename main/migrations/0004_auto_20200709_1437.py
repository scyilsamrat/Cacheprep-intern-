# Generated by Django 2.2.2 on 2020-07-09 09:07

from django.db import migrations, models
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200709_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Q_id', models.CharField(max_length=10, unique=True)),
                ('Q_text', models.CharField(max_length=100, unique=True)),
                ('Q_img', models.ImageField(upload_to=main.models.Questions.upload_dir)),
                ('Q_tag', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Quetions',
        ),
    ]
