# Generated by Django 2.1.7 on 2019-02-20 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0002_auto_20190219_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='postcomment',
            name='mention',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_mentions', related_query_name='comment_mention', to=settings.AUTH_USER_MODEL),
        ),
    ]