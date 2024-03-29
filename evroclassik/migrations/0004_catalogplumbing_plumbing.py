# Generated by Django 2.2.3 on 2019-07-21 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('evroclassik', '0003_furniture_name_furniture'),
    ]

    operations = [
        migrations.CreateModel(
            name='CatalogPlumbing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=200)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plumbing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_plumbing', models.CharField(blank=True, max_length=50)),
                ('price', models.IntegerField()),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evroclassik.CatalogPlumbing')),
            ],
            options={
                'verbose_name_plural': 'plumbings',
            },
        ),
    ]
