# Generated by Django 3.2 on 2021-04-15 00:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_alter_author_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.UUIDField(default=uuid.UUID('761387c5-5fcb-475d-9a3b-03b8b9e1effd'), editable=False, primary_key=True, serialize=False),
        ),
    ]
