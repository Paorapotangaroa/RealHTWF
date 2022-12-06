# Generated by Django 4.1.2 on 2022-12-06 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HTWFApp.author')),
            ],
            options={
                'db_table': 'story',
            },
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=2000)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HTWFApp.story')),
            ],
            options={
                'db_table': 'paragraph',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('text', models.CharField(max_length=2000)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HTWFApp.story')),
            ],
            options={
                'db_table': 'comment',
            },
        ),
    ]
