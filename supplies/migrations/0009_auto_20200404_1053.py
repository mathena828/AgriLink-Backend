# Generated by Django 3.0.4 on 2020-04-04 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplies', '0008_auto_20200404_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='code',
            field=models.CharField(default='pbkdf2_sha256$180000$QbGCAqPydOCb$uUYHRNlOGQwcRPMdytl4R6/JQo+8kfsi8yripeI9dYA=', max_length=20),
        ),
    ]
