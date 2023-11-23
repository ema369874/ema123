# Generated by Django 4.2.7 on 2023-11-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrackedClick',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('click_id', models.CharField(max_length=255)),
                ('offer_id', models.CharField(max_length=255)),
                ('user_id', models.CharField(max_length=255)),
                ('ip_address', models.GenericIPAddressField()),
                ('country', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
