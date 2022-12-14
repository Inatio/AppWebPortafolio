# Generated by Django 2.2.10 on 2022-11-24 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'cargo1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Comuna1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'comuna1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contacto1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'contacto1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('imagen', models.ImageField(null=True, upload_to='departamentos')),
                ('direccion', models.CharField(max_length=25)),
                ('numero', models.CharField(max_length=5)),
                ('torre', models.CharField(blank=True, max_length=12, null=True)),
            ],
            options={
                'db_table': 'departamento1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DiferenciaPago1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'diferencia_pago1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Funcionario1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=25)),
                ('segundo_nombre', models.CharField(max_length=25)),
                ('apellido_paterno', models.CharField(max_length=25)),
                ('apellido_materno', models.CharField(max_length=25)),
                ('rut', models.CharField(max_length=12)),
                ('acta_de_check_out_id', models.IntegerField(db_column='Acta de check-out_id')),
            ],
            options={
                'db_table': 'funcionario1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PagoInicial1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'pago_inicial1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Region1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('nombre', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'region1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reportes1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'reportes1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reserva1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(blank=True, null=True)),
                ('dias', models.IntegerField()),
                ('procesado', models.CharField(blank=True, max_length=1, null=True)),
            ],
            options={
                'db_table': 'reserva1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Reservas1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'reservas1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoPago1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'tipo_pago1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoReporte1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tipo_reporte1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoTour1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
                ('codigo', models.IntegerField()),
            ],
            options={
                'db_table': 'tipo_tour1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoTransporte1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'tipo_transporte1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TotalDePago1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'total_de_pago1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tour1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'tour1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Transporte1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'transporte1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('contrase??a', models.CharField(max_length=15)),
                ('correo', models.CharField(max_length=25)),
                ('celular', models.IntegerField()),
            ],
            options={
                'db_table': 'usuario1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Vehiculo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patente', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'vehiculo1',
                'managed': False,
            },
        ),
    ]
