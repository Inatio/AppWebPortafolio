# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cargo(models.Model):
    codigo = models.IntegerField()
    nombrecargo = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'cargo'


class Comuna(models.Model):
    id_comuna = models.IntegerField(primary_key=True)
    nombre_comuna = models.CharField(max_length=50)
    id_region = models.ForeignKey('Region', models.DO_NOTHING, db_column='id_region')

    class Meta:
        managed = False
        db_table = 'comuna'


class Contacto(models.Model):
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    descripcion = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'contacto'


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


class Disponibilidad(models.Model):
    id_disp = models.AutoField(primary_key=True)
    descr_estado = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'disponibilidad'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class InventarioDpto(models.Model):
    id_inv = models.AutoField(primary_key=True)
    id_dpto = models.ForeignKey(Departamento, models.DO_NOTHING, db_column='id_dpto')
    nombre_objeto = models.CharField(max_length=50)
    cant_objeto = models.IntegerField()
    valor_unitario_obj = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventario_dpto'


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


class Pago(models.Model):
    pago_inicial = models.IntegerField(blank=True, null=True)
    diferencia_pago = models.IntegerField(blank=True, null=True)
    total_pagar = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pago'


class Region(models.Model):
    id_region = models.IntegerField(primary_key=True)
    nombre_region = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'region'


class Reserva(models.Model):
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING)
    departamento = models.ForeignKey(Departamento, models.DO_NOTHING)
    tour = models.ForeignKey('Tour', models.DO_NOTHING)
    total_pagar = models.ForeignKey(Pago, models.DO_NOTHING, db_column='total_pagar', blank=True, null=True)
    dias = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'reserva'


class TipoTour(models.Model):
    descripcion = models.CharField(max_length=100)
    codigo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_tour'


class Tour(models.Model):
    tipo_tour = models.ForeignKey(TipoTour, models.DO_NOTHING, db_column='tipo tour_id')  # Field renamed to remove unsuitable characters.
    funcionario_id = models.IntegerField()
    valor = models.IntegerField()
    id_usuario = models.ForeignKey('UsuarioFunc', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tour'


class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=25)
    correo = models.CharField(max_length=100)
    celular = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'usuario'


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


class Vehiculo(models.Model):
    id_vehiculo = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=6)
    codigo = models.IntegerField()
    descripcion = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(UsuarioFunc, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vehiculo'
