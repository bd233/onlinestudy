# Generated by Django 2.1.1 on 2019-04-14 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0015_auto_20190414_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='education',
            field=models.IntegerField(blank=True, choices=[(0, '大专'), (1, '本科'), (2, '研究生'), (3, '博士'), (4, '硕士'), (5, '其他')], null=True, verbose_name='学历'),
        ),
    ]
