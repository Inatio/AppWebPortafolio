# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cargo1(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cargo1'


class Comuna1(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'comuna1'
    
    def __str__(self): return self.nombre


class Contacto1(models.Model):
    usuario = models.ForeignKey('Usuario1', models.DO_NOTHING)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'contacto1'


class Departamento1(models.Model):
    region = models.ForeignKey('Region1', models.DO_NOTHING)
    comuna = models.ForeignKey(Comuna1, models.DO_NOTHING)
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="departamentos", null=True)
    direccion = models.CharField(max_length=25)
    numero = models.CharField(max_length=5)
    torre = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento1'

    def __str__(self): return self.descripcion


class DiferenciaPago1(models.Model):
    tipo_pago = models.ForeignKey('TipoPago1', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'diferencia_pago1'


class Funcionario1(models.Model):
    cargo = models.ForeignKey(Cargo1, models.DO_NOTHING)
    transporte = models.ForeignKey('Transporte1', models.DO_NOTHING)
    reportes = models.ForeignKey('Reportes1', models.DO_NOTHING)
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=25)
    segundo_nombre = models.CharField(max_length=25)
    apellido_paterno = models.CharField(max_length=25)
    apellido_materno = models.CharField(max_length=25)
    rut = models.CharField(max_length=12)
    acta_de_check_out_id = models.IntegerField(db_column='Acta de check-out_id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    contacto = models.ForeignKey(Contacto1, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'funcionario1'


class PagoInicial1(models.Model):
    tipo_pago = models.ForeignKey('TipoPago1', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'pago_inicial1'


class Region1(models.Model):
    codigo = models.IntegerField()
    nombre = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'region1'
    
    def __str__(self): return self.nombre


class Reportes1(models.Model):
    tipo_reporte = models.ForeignKey('TipoReporte1', models.DO_NOTHING, db_column='Tipo reporte_id')  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'reportes1'


class Reserva1(models.Model):
    usuario = models.ForeignKey('Usuario1', models.DO_NOTHING)
    departamento = models.ForeignKey(Departamento1, models.DO_NOTHING)
    reportes = models.ForeignKey(Reportes1, models.DO_NOTHING)
    tour = models.ForeignKey('Tour1', models.DO_NOTHING)
    total = models.IntegerField(blank=True, null=True)
    dias = models.IntegerField()
    procesado = models.CharField(max_length=1, blank=True, null=True)
    total_de_pago = models.ForeignKey('TotalDePago1', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reserva1'


class Reservas1(models.Model):
    reserva = models.ForeignKey(Reserva1, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'reservas1'


class TipoPago1(models.Model):

    class Meta:
        managed = False
        db_table = 'tipo_pago1'


class TipoReporte1(models.Model):
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_reporte1'

    def __str__(self): return self.descripcion


class TipoTour1(models.Model):
    descripcion = models.CharField(max_length=100)
    codigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_tour1'

    def __str__(self): return self.descripcion



class TipoTransporte1(models.Model):
    vehiculo = models.ForeignKey('Vehiculo1', models.DO_NOTHING)
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'tipo_transporte1'

    def __str__(self): return self.descripcion


class TotalDePago1(models.Model):
    diferencia_pago = models.ForeignKey(DiferenciaPago1, models.DO_NOTHING, db_column='Diferencia pago_id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pago_inicial = models.ForeignKey(PagoInicial1, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'total_de_pago1'


class Tour1(models.Model):
    tipo_tour = models.ForeignKey(TipoTour1, models.DO_NOTHING, db_column='Tipo tour_id')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    funcionario = models.ForeignKey(Funcionario1, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tour1'


class Transporte1(models.Model):
    tipo_transporte = models.ForeignKey(TipoTransporte1, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'transporte1'


class Usuario1(models.Model):
    nombre = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=15)
    correo = models.CharField(max_length=25)
    celular = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario1'

    def __str__(self): return self.correo


class Vehiculo1(models.Model):
    patente = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'vehiculo1'

    def __str__(self): return self.patente
