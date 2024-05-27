# Generated by Django 5.0.3 on 2024-05-24 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(choices=[('남자', '남자'), ('여자', '여자')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='user',
            name='generation',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
