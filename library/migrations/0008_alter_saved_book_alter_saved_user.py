# Generated by Django 4.1.1 on 2022-09-15 19:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_rename_savedlist_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='saved',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to='library.book'),
        ),
        migrations.AlterField(
            model_name='saved',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to=settings.AUTH_USER_MODEL),
        ),
    ]
