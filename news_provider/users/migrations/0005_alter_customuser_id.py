# Generated by Django 3.2 on 2021-04-18 00:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_customuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('56ddc934-6393-45fb-b51d-f758f32b4f16'), editable=False, primary_key=True, serialize=False),
        ),
    ]
