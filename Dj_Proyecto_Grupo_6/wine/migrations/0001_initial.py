# Generated by Django 3.2.18 on 2023-06-05 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id_categoria', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
                ('agrupado', models.CharField(choices=[('tinto', 'TINTO'), ('blanco', 'BLANCO'), ('espumante', 'ESPUMANTE')], default='tinto', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('contacto', models.AutoField(primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=20)),
                ('telefono', models.CharField(max_length=100)),
                ('consulta', models.BooleanField(default=False)),
                ('comentario', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Precio',
            fields=[
                ('id_precio', models.IntegerField(primary_key=True, serialize=False)),
                ('fe_desde', models.DateField()),
                ('fe_hasta', models.DateField()),
                ('precio', models.FloatField()),
                ('desc_xcaja', models.FloatField()),
                ('promo', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=250)),
                ('conservacion', models.CharField(max_length=250)),
                ('bodega', models.CharField(default='', max_length=100)),
                ('id_categoria', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wine.categoria')),
                ('id_precio', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wine.precio')),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveBigIntegerField()),
                ('id_producto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='wine.producto')),
            ],
        ),
    ]
