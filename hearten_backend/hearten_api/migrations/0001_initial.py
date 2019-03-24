# Generated by Django 2.1.7 on 2019-03-24 12:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('imagePrompt', models.CharField(blank=True, max_length=100)),
                ('textPrompt', models.CharField(blank=True, max_length=100)),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
