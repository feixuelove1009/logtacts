# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-10-18 21:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_auto_20161016_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeCharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('stripe_id', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('succeeded', 'succeeded'), ('failed', 'failed')], default='pending', max_length=100)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=10, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.StripeCustomer')),
            ],
        ),
        migrations.CreateModel(
            name='StripeInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('changed', models.DateTimeField(auto_now=True)),
                ('stripe_id', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('succeeded', 'succeeded'), ('failed', 'failed')], default='pending', max_length=100)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('currency', models.CharField(blank=True, max_length=10, null=True)),
                ('charge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.StripeCharge')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.StripeCustomer')),
                ('subscriptions', models.ManyToManyField(to='payments.StripeSubscription')),
            ],
        ),
        migrations.AddField(
            model_name='stripecharge',
            name='invoice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payments.StripeInvoice'),
        ),
    ]