# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-10 21:45
from __future__ import unicode_literals

from django.db import migrations


def cleanup_submissions(apps, schema_editor):
    subs = apps.get_model("pootle_statistics.Submission").objects.all()
    subs.filter(unit__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('pootle_statistics', '0010_submission_on_delete_user'),
    ]

    operations = [
        migrations.RunPython(cleanup_submissions),
    ]