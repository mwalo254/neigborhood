# Generated by Django 3.1.2 on 2020-10-30 15:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pic/')),
                ('description', models.TextField(max_length=100)),
                ('police_contact', models.IntegerField(default='112')),
                ('hospital_contact', models.IntegerField(default='911')),
                ('population', models.IntegerField(default='10')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('bio', tinymce.models.HTMLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='pic/')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=80)),
                ('description', models.TextField(max_length=150)),
                ('image', models.ImageField(upload_to='pic/')),
                ('hood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nebapp.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='admin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nebapp.profile'),
        ),
        migrations.AddField(
            model_name='neighbourhood',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nebapp.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=40)),
                ('business_description', models.TextField(max_length=100)),
                ('business_email', models.EmailField(max_length=254)),
                ('admin', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nebapp.profile')),
                ('hood', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nebapp.neighbourhood')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
