# Generated by Django 4.2.2 on 2023-06-10 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, max_length=512, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('deleted', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', related_query_name='product', to='products.product')),
            ],
            options={
                'verbose_name': 'product_image',
                'verbose_name_plural': 'product_images',
            },
        ),
    ]
