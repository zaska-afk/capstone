# Generated by Django 3.2.7 on 2021-10-08 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0001_initial'),
        ('project', '0002_auto_20211008_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='comm_creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authuser.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authuser.profile'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='vote_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authuser.profile'),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]