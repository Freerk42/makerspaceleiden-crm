# Generated by Django 2.1.4 on 2018-12-07 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_historicalentitlement_historicalmember_historicalpermittype_historicaltag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entitlement',
            name='holder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isGivenTo', to='members.Member'),
        ),
        migrations.AlterField(
            model_name='entitlement',
            name='issuer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='isIssuedBy', to='members.Member'),
        ),
        migrations.AlterField(
            model_name='historicalentitlement',
            name='holder',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='members.Member'),
        ),
        migrations.AlterField(
            model_name='historicalentitlement',
            name='issuer',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='members.Member'),
        ),
    ]
