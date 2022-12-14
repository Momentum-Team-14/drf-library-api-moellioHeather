# Generated by Django 4.1.1 on 2022-09-14 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('genres', models.ManyToManyField(related_name='books', to='library.genre')),
            ],
        ),
    ]
