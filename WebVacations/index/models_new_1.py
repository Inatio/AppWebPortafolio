# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cargo(models.Model):
    codigo = models.IntegerField()
    nombrecargo = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cargo'

    def __str__(self):
        return "{}".format(self.nombrecargo)


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=50)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comuna'

    def __str__(self):
        return "{}".format(self.nombre_comuna)


class Contacto(models.Model):
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'contacto'

    def __str__(self):
        return "{}".format(self.descripcion)


class Departamento(models.Model):
    id_dpto = models.AutoField(primary_key=True)
    nombre_dpto = models.CharField(max_length=100)
    tarifa_diaria = models.IntegerField()
    direccion = models.CharField(max_length=20)
    nro_dpto = models.IntegerField()
    capacidad = models.IntegerField()
    id_comuna = models.ForeignKey(Comuna, models.DO_NOTHING, db_column='id_comuna')
    disponibilidad = models.ForeignKey('Disponibilidad', models.DO_NOTHING, db_column='disponibilidad', blank=True, null=True)
    imagen = models.ImageField(upload_to="departamentos", null=True)
    img = models.BinaryField(blank=True, null=True)
    img1 = models.BinaryField(blank=True, null=True)
    img2 = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'departamento'

    def __str__(self):
        return "{}".format(self.nombre_dpto)


class Disponibilidad(models.Model):
    id_disp = models.AutoField(primary_key=True)
    descr_estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'disponibilidad'

    def __str__(self):
        return "{}".format(self.descr_estado)


class InventarioDpto(models.Model):
    id_inv = models.AutoField(primary_key=True)
    id_dpto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_dpto')
    nombre_objeto = models.CharField(max_length=50)
    cant_objeto = models.IntegerField()
    valor_unitario_obj = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventario_dpto'

    def __str__(self):
        return "{}".format(self.nombre_objeto)


class Mantenimiento(models.Model):
    id_mant = models.AutoField(primary_key=True)
    id_dpto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_dpto')
    nombre_mant = models.CharField(max_length=50)
    descripcion_mant = models.CharField(max_length=2000)
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    disponibilidad = models.IntegerField()
    costo_mantencion = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mantenimiento'

    def __str__(self):
        return "{}".format(self.nombre_mant)


class Pago(models.Model):
    pago_inicial = models.IntegerField(blank=True, null=True)
    diferencia_pago = models.IntegerField(blank=True, null=True)
    total_pagar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'

    def __str__(self):
        return "{}".format(self.total_pagar)


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'

    def __str__(self):
        return "{}".format(self.nombre_region)


class Reserva(models.Model):
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)
    tour = models.ForeignKey('Tour', models.DO_NOTHING)
    total_pagar = models.ForeignKey(Pago, models.DO_NOTHING, db_column='total_pagar', blank=True, null=True)
    dias = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reserva'

    def __str__(self):
        return "{}".format(self.usuario)


class TipoTour(models.Model):
    descripcion = models.CharField(max_length=100)
    codigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_tour'

    def __str__(self):
        return "{}".format(self.descripcion)


class Tour(models.Model):
    tipo_tour = models.ForeignKey(TipoTour, models.DO_NOTHING, db_column='tipo tour_id')  # Field renamed to remove unsuitable characters.
    funcionario_id = models.IntegerField()
    valor = models.IntegerField()
    id_usuario = models.ForeignKey('UsuarioFunc', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'

    def __str__(self):
        return "{}".format(self.tipo_tour)


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=25)
    correo = models.CharField(max_length=100)
    celular = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'

    def __str__(self):
        return "{}".format(self.correo)


class UsuarioFunc(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    email = models.CharField(max_length=254)
    clave = models.CharField(max_length=40)
    celular = models.IntegerField()
    rut = models.CharField(max_length=14)
    nombres = models.CharField(max_length=40)
    apellidopaterno = models.CharField(max_length=40)
    apellidomaterno = models.CharField(max_length=40)
    img = models.BinaryField(blank=True, null=True)
    idcargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='idcargo')

    class Meta:
        managed = False
        db_table = 'usuario_func'

    def __str__(self):
        return "{}".format(self.email)


class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=6)
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(UsuarioFunc, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehiculo'
    
    def __str__(self):
        return "{}".format(self.patente)
