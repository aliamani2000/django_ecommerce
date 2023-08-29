# Generated by Django 4.1.3 on 2022-12-13 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('restored_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False, editable=False)),
                ('is_active', models.BooleanField(default=True, editable=False)),
                ('name', models.CharField(max_length=255, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('city', models.CharField(choices=[('Tehran', 'Tehran'), ('Esfahan', 'Esfahan'), ('Qom', 'Qom'), ('Mashhad', 'Mashhad'), ('Shiraz', 'Shiraz'), ('Tabriz', 'Tabriz'), ('Kerman', 'Kerman'), ('Ahvaz', 'Ahvaz')], default='Tehran', max_length=255)),
                ('time', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Shipping',
                'verbose_name_plural': 'Shipping',
            },
        ),
    ]
