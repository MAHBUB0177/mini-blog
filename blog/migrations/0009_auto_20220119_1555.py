# Generated by Django 3.2.6 on 2022-01-19 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_albums_musician'),
    ]

    operations = [
        migrations.RenameField(
            model_name='albums',
            old_name='tags',
            new_name='musician',
        ),
        migrations.AlterField(
            model_name='albums',
            name='artist',
            field=models.ForeignKey(db_column='artist', on_delete=django.db.models.deletion.CASCADE, related_name='album_name', to='blog.musician'),
        ),
    ]