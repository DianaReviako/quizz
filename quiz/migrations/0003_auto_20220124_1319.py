# Generated by Django 3.2.1 on 2022-01-24 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_question_question_assessment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_assessment',
            new_name='assessment',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='topic_title',
            new_name='topic',
        ),
        migrations.RenameField(
            model_name='topic',
            old_name='topic_title',
            new_name='title',
        ),
    ]