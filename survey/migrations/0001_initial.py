# Generated by Django 5.0.9 on 2024-12-10 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('question_type', models.CharField(default='boolean', max_length=20)),
                ('options', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
