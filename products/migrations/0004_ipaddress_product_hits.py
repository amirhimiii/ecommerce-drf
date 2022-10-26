# Generated by Django 4.1.1 on 2022-10-14 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='IPAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='view count:')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hits', to='products.ipaddress'),
        ),
    ]
