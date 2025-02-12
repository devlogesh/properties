# Generated by Django 5.1.3 on 2025-01-24 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('propertiesapp', '0008_remove_propertymedia_property_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='created_by_id',
            field=models.ForeignKey(blank=True, db_column='created_by_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='propertiesapp.userprofile'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='customer_number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='updated_by_id',
            field=models.ForeignKey(blank=True, db_column='updated_by_id', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='propertiesapp.userprofile'),
        ),
        migrations.AlterField(
            model_name='farmlandproperty',
            name='area',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmlandproperty',
            name='distance_from_road',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='farmlandproperty',
            name='electricity',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmlandproperty',
            name='encumbrance_certificate',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmlandproperty',
            name='negotiable',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='farmlandproperty',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='area',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='balcony',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='bathrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='distance_from_road',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='encumbrance_certificate',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='floor_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='negotiable',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='power_backup',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='houseproperty',
            name='total_floors',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotproperty',
            name='area',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotproperty',
            name='distance_from_road',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='plotproperty',
            name='east_west_length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='plotproperty',
            name='encumbrance_certificate',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotproperty',
            name='negotiable',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotproperty',
            name='north_south_length',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
        migrations.AlterField(
            model_name='plotproperty',
            name='plot_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='plotproperty',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=19, null=True),
        ),
    ]
