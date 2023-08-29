# Generated by Django 4.1.3 on 2022-12-13 11:45

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('restored_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('body', models.TextField()),
                ('city', models.CharField(choices=[('Tehran', 'Tehran'), ('Esfahan', 'Esfahan'), ('Qom', 'Qom'), ('Mashhad', 'Mashhad'), ('Shiraz', 'Shiraz'), ('Tabriz', 'Tabriz'), ('Kerman', 'Kerman'), ('Ahvaz', 'Ahvaz')], default='Tehran', max_length=255)),
            ],
            options={
                'verbose_name': 'Address',
                'verbose_name_plural': 'Addresses',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('restored_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('phone', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('image', models.ImageField(blank=True, default='profile_images/default.png', null=True, upload_to='profile_images')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='user_profile.address')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
    ]
