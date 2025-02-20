# Generated by Django 3.1.2 on 2020-10-26 14:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=200)),
                ('People', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.people')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('People', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contact.people')),
            ],
        ),
    ]
