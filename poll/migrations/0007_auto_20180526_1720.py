# Generated by Django 2.0.4 on 2018-05-26 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0006_auto_20180516_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(null=True)),
                ('score', models.IntegerField(null=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.Menu')),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='user',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='user',
            name='score',
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='commentscore',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poll.User'),
        ),
    ]
