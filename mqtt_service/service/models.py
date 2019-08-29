# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
import uuid



class Clientes(models.Model):
    id_cliente_internal = models.BigIntegerField(primary_key=True)
    id_cliente_uuid = models.UUIDField()
    id_cliente_external = models.IntegerField()
    id_documentos_tipos = models.IntegerField()
    numero_documento = models.BigIntegerField()
    nombre_cliente = models.CharField(max_length=255)
    direccion_principal = models.CharField(max_length=255)
    id_ciudad = models.IntegerField()
    id_departamento = models.IntegerField()
    id_pais = models.IntegerField()
    comentarios_cliente = models.TextField(blank=True, null=True)
    cliente_bloqueado = models.BooleanField(blank=True, null=True)
    cliente_activo = models.BooleanField(blank=True, null=True)
    fecha_no_activo = models.DateField(blank=True, null=True)
    fechahora_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'
        app_label = 'api'


class ClientesContactos(models.Model):
    id_cliente_contacto = models.AutoField(primary_key=True)
    id_cliente_internal = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente_internal')
    id_cliente_contacto_tipo = models.ForeignKey('ClientesContactosTipos', models.DO_NOTHING, db_column='id_cliente_contacto_tipo')
    nombre_contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono_fijo_contacto = models.CharField(max_length=15, blank=True, null=True)
    celular_contacto = models.CharField(max_length=15, blank=True, null=True)
    email_contacto = models.CharField(max_length=254, blank=True, null=True)
    detalles_contacto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_contactos'
        app_label = 'api'


class ClientesContactosTipos(models.Model):
    id_cliente_contacto_tipo = models.AutoField(primary_key=True)
    tipo_contacto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_contactos_tipos'
        app_label = 'api'


class ClientesDispositivos(models.Model):
    id_cliente_internal = models.ForeignKey(Clientes, on_delete=models.CASCADE, db_column='id_cliente_internal')
    id_dispositivo = models.OneToOneField('Dispositivos', on_delete=models.CASCADE, db_column='id_dispositivo', primary_key=True)
    nombre_corto_cliente_dispositivo = models.CharField(max_length=50, blank=True, null=True)
    localizacion_cliente_dispositivo = models.CharField(max_length=50, blank=True, null=True)
    detalle_dispositivo = models.TextField(blank=True, null=True)
    fechahora_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes_dispositivos'
        unique_together = (('id_dispositivo', 'id_cliente_internal'),)
        app_label = 'api'


class ComunicacionesEstrategias(models.Model):
    id_comunicacion_estrategia = models.AutoField(primary_key=True)
    nombre_estrategia = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'comunicaciones_estrategias'
        app_label = 'api'


class ComunicacionesMedios(models.Model):
    id_comunicacion_medio = models.AutoField(primary_key=True)
    tipo_medio = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'comunicaciones_medios'
        app_label = 'api'


class ComunicacionesMssgsEnviadas(models.Model):
    id_comm_mssg_enviada = models.BigIntegerField(primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario')
    id_comm_medio_interno = models.ForeignKey('UsuariosComunicacion', models.DO_NOTHING, db_column='id_comm_medio_interno')
    mssg_enviada = models.TextField(blank=True, null=True)
    mssg_enviada_fechahora = models.DateTimeField()
    time_utc_epc_pub = models.FloatField(blank=True, null=True)
    time_utc_epc_mssg_enviada = models.FloatField(blank=True, null=True)
    id_dispositivos_notificaciones = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunicaciones_mssgs_enviadas'
        app_label = 'api'


class ComunicacionesNotificaciones(models.Model):
    id_notificacion = models.OneToOneField('Notificaciones', on_delete=models.CASCADE, db_column='id_notificacion', primary_key=True)
    id_comunicacion_medio = models.ForeignKey(ComunicacionesMedios, on_delete=models.CASCADE, db_column='id_comunicacion_medio')
    id_comunicacion_estrategia = models.ForeignKey(ComunicacionesEstrategias, on_delete=models.CASCADE, db_column='id_comunicacion_estrategia')
    class Meta:
        managed = False
        db_table = 'comunicaciones_notificaciones'
        unique_together = (('id_notificacion', 'id_comunicacion_medio', 'id_comunicacion_estrategia'),)
        app_label = 'api'


class Dispositivos(models.Model):
    id_dispositivo = models.BigIntegerField(primary_key=True)
    numero_serie = models.CharField(unique=True, max_length=20)
    id_mqtt = models.CharField(unique=True, max_length=20, blank=True, null=True)
    imei = models.CharField(unique=True, max_length=15, blank=True, null=True)
    id_dispositivo_modelo_internal = models.ForeignKey('DispositivosModelos', models.DO_NOTHING, db_column='id_dispositivo_modelo_internal', blank=True, null=True)
    id_dispositivo_lote = models.ForeignKey('DispositivosLotes', models.DO_NOTHING, db_column='id_dispositivo_lote', blank=True, null=True)
    id_sim_card = models.ForeignKey('OperadoresCelularesSimCards', models.DO_NOTHING, db_column='id_sim_card', blank=True, null=True)
    status_inicializado = models.BooleanField(blank=True, null=True)
    status_dispositivo = models.BooleanField(blank=True, null=True)
    fechahora_activacion = models.DateTimeField(blank=True, null=True)
    fechahora_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos'
        app_label = 'api'


class DispositivosLotes(models.Model):
    id_dispositivo_lote = models.AutoField(primary_key=True)
    codigo_lote = models.CharField(max_length=5, blank=True, null=True)
    unidades_lote = models.IntegerField()
    fecha_inicial_fabr_lote = models.DateField()
    fecha_final_fabr_lote = models.DateField(blank=True, null=True)
    detalles_lote = models.TextField(blank=True, null=True)
    fechahora_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_lotes'
        app_label = 'api'


class DispositivosModelos(models.Model):
    id_dispositivo_modelo_internal = models.AutoField(primary_key=True)
    id_dispositivo_modelo_external = models.CharField(max_length=5)
    nombre_modelo = models.CharField(max_length=20, blank=True, null=True)
    id_dispositivo_tipo = models.ForeignKey('DispositivosTipos', models.DO_NOTHING, db_column='id_dispositivo_tipo')
    version_hardware_dispositivo = models.CharField(max_length=10)
    version_software_dispositivo = models.CharField(max_length=10)
    detalles_dispositivo = models.TextField(blank=True, null=True)
    fechahora_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_modelos'
        app_label = 'api'


class DispositivosModelosPuertosBasicos(models.Model):
    id_dispositivo_modelo = models.CharField(primary_key=True, max_length=5)
    id_modelo_puerto = models.IntegerField()
    cantidad_puertos = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'dispositivos_modelos_puertos_basicos'
        unique_together = (('id_dispositivo_modelo', 'id_modelo_puerto'),)
        app_label = 'api'


class DispositivosNotificaciones(models.Model):
    id_dispositivos_notificaciones = models.BigIntegerField(primary_key=True)
    id_notificacion = models.ForeignKey('Notificaciones', models.DO_NOTHING, db_column='id_notificacion')
    id_dispositivo = models.ForeignKey(Dispositivos, models.DO_NOTHING, db_column='id_dispositivo')
    id_alerta_nivel = models.ForeignKey('NotificacionesAlertaNiveles', models.DO_NOTHING, db_column='id_alerta_nivel')
    id_mssg_mqtt = models.BigIntegerField()
    id_usuario = models.ForeignKey('Usuarios', models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    id_dispositivo_ubicacion = models.ForeignKey('DispositivosUbicaciones', models.DO_NOTHING, db_column='id_dispositivo_ubicacion', blank=True, null=True)
    id_dispositivo_puerto = models.ForeignKey('DispositivosPuertos', models.DO_NOTHING, db_column='id_dispositivo_puerto', blank=True, null=True)
    valor_medida_notificacion = models.FloatField(blank=True, null=True)
    time_utc_pub = models.DateTimeField()
    time_utc_epc_pub = models.FloatField()
    time_utc_epc_load = models.FloatField()
    comm_prcssd = models.BooleanField()
    time_utc_comm_prcssd = models.DateTimeField(blank=True, null=True)
    time_utc_epc_comm_prcssd = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_notificaciones'
        app_label = 'api'


class DispositivosPuertos(models.Model):
    id_dispositivo_puerto = models.AutoField(primary_key=True)
    id_dispositivo = models.ForeignKey(Dispositivos, models.DO_NOTHING, db_column='id_dispositivo')
    cod_puerto_dispo = models.CharField(max_length=5)
    id_modelo_puerto = models.ForeignKey('DispositivosPuertosModelosTipos', models.DO_NOTHING, db_column='id_modelo_puerto')
    nombre_puerto = models.CharField(max_length=50)
    descripcion_puerto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_puertos'
        unique_together = (('id_dispositivo', 'cod_puerto_dispo'),)
        app_label = 'api'


class DispositivosPuertosModelosTipos(models.Model):
    id_modelo_puerto = models.AutoField(primary_key=True)
    modelo_puerto_codigo = models.CharField(max_length=5, blank=True, null=True)
    modelo_puerto_nombre = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_puertos_modelos_tipos'
        app_label = 'api'


class DispositivosTipos(models.Model):
    id_dispositivo_tipo = models.AutoField(primary_key=True)
    tipo_dispositivo = models.CharField(unique=True, max_length=50)
    fechahora_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_tipos'
        app_label = 'api'


class DispositivosUbicaciones(models.Model):
    id_dispositivo_ubicacion = models.AutoField(primary_key=True)
    id_dispositivo = models.ForeignKey(Dispositivos, models.DO_NOTHING, db_column='id_dispositivo')
    cod_ubicacion_nivel1 = models.SmallIntegerField()
    cod_ubicacion_nivel2 = models.SmallIntegerField()
    nombre_corto_ubicacion_nivel1 = models.CharField(max_length=50, blank=True, null=True)
    nombre_corto_ubicacion_nivel2 = models.CharField(max_length=50, blank=True, null=True)
    detalle_ubicacion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_ubicaciones'
        unique_together = (('id_dispositivo', 'cod_ubicacion_nivel1', 'cod_ubicacion_nivel2'),)
        app_label = 'api'


class DispositivosUsuariosReferenciaCliente(models.Model):
    id_dispositivo_usuario_autonumber = models.IntegerField(default=1)
    id_dispositivo = models.OneToOneField(Dispositivos, on_delete=models.CASCADE, db_column='id_dispositivo', primary_key=True)
    id_usuario = models.ForeignKey('Usuarios', on_delete=models.CASCADE, db_column='id_usuario')
    id_dispositivo_usuario_referencia_cliente = models.IntegerField(blank=True, null=True)
    observacion_dispositivo_usuario = models.TextField(blank=True, null=True)
    usuario_puede_leer_dispositivo = models.BooleanField()
    usuario_puede_editar_dispositivo = models.BooleanField()

    def save(self, *args, **kwargs):
        if self._state.adding:
            last_id_dispositivo_usuario_autonumber = self.objects.all().aggregate(largest=models.Max('display_id'))['largest']
            if last_id_dispositivo_usuario_autonumber is not None:
                self.id_dispositivo_usuario_autonumber = last_id_dispositivo_usuario_autonumber + 1
        super(DispositivosUsuariosReferenciaCliente, self).save(*args, **kwargs)

    class Meta:
        managed = False
        db_table = 'dispositivos_usuarios_referencia_cliente'
        unique_together = (('id_dispositivo', 'id_usuario'),)
        app_label = 'api'


class DispositivosUsuariosSinReferencia(models.Model):
    id_dispositivo = models.ForeignKey(Dispositivos, models.DO_NOTHING, db_column='id_dispositivo')
    id_dispositivo_usuario_referencia_cliente = models.IntegerField(blank=True, null=True)
    time_utc_pub = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivos_usuarios_sin_referencia'
        app_label = 'api'


class DocumentosTipos(models.Model):
    id_documentos_tipos = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=30)
    documento_persona_natural = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentos_tipos'
        app_label = 'api'


class Notificaciones(models.Model):
    id_notificacion = models.IntegerField(primary_key=True)
    id_notificacion_tipo = models.ForeignKey('NotificacionesTipos', models.DO_NOTHING, db_column='id_notificacion_tipo')
    cod_notificacion = models.CharField(max_length=5)
    nombre_notificacion = models.CharField(max_length=50)
    detalle_notificacion = models.CharField(max_length=200, blank=True, null=True)
    id_alerta_nivel_base = models.ForeignKey('NotificacionesAlertaNiveles', models.DO_NOTHING, db_column='id_alerta_nivel_base', blank=True, null=True)
    notificacion_icon_front = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificaciones'
        app_label = 'api'


class NotificacionesAlertaNiveles(models.Model):
    id_alerta_nivel = models.IntegerField(primary_key=True)
    alerta_nivel_severidad = models.CharField(max_length=30, blank=True, null=True)
    alerta_nivel_informacion = models.CharField(max_length=30, blank=True, null=True)
    alerta_nivel_color = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificaciones_alerta_niveles'
        app_label = 'api'


class NotificacionesTipos(models.Model):
    id_tipo_notificacion = models.AutoField(primary_key=True)
    tipo_notificacion = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificaciones_tipos'
        app_label = 'api'


class OperadoresCelulares(models.Model):
    id_operador_celular = models.AutoField(primary_key=True)
    operador_celular = models.CharField(max_length=30, blank=True, null=True)
    id_pais = models.ForeignKey('Paises', models.DO_NOTHING, db_column='id_pais')

    class Meta:
        managed = False
        db_table = 'operadores_celulares'
        app_label = 'api'


class OperadoresCelularesPlanesDatos(models.Model):
    id_plan_datos = models.SmallIntegerField(primary_key=True)
    plan_datos_nombre = models.CharField(max_length=100)
    id_operador_celular = models.ForeignKey(OperadoresCelulares, models.DO_NOTHING, db_column='id_operador_celular')

    class Meta:
        managed = False
        db_table = 'operadores_celulares_planes_datos'
        app_label = 'api'


class OperadoresCelularesSimCards(models.Model):
    id_sim_card = models.AutoField(primary_key=True)
    id_serial_sim = models.BigIntegerField(blank=True, null=True)
    numero_celular = models.CharField(unique=True, max_length=15)
    id_operadora_celular = models.ForeignKey(OperadoresCelulares, models.DO_NOTHING, db_column='id_operadora_celular')
    id_plan_datos = models.ForeignKey(OperadoresCelularesPlanesDatos, models.DO_NOTHING, db_column='id_plan_datos', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'operadores_celulares_sim_cards'
        app_label = 'api'


class Paises(models.Model):
    id_pais = models.AutoField(primary_key=True)
    iso = models.CharField(max_length=2)
    nombre_pais_iso = models.CharField(max_length=80)
    nombre_pais_esp = models.CharField(max_length=80, blank=True, null=True)
    nombre_pais_ing = models.CharField(max_length=80)
    iso3 = models.CharField(max_length=3, blank=True, null=True)
    numcode = models.SmallIntegerField(blank=True, null=True)
    phonecode = models.SmallIntegerField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'paises'
        app_label = 'api'


class PaisesCiudades(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    cod_ciudad_pais = models.CharField(max_length=20, blank=True, null=True)
    id_departamento = models.ForeignKey('PaisesDepartamentos', models.DO_NOTHING, db_column='id_departamento')
    id_departamento_pais = models.SmallIntegerField(blank=True, null=True)
    nombre_ciudad = models.CharField(max_length=100)
    region_ciudad = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'paises_ciudades'
        app_label = 'api'


class PaisesDepartamentos(models.Model):
    id_departamento = models.AutoField(primary_key=True)
    id_departamento_pais = models.SmallIntegerField()
    departamento = models.CharField(max_length=100)
    id_pais = models.ForeignKey(Paises, models.DO_NOTHING, db_column='id_pais')

    class Meta:
        managed = False
        db_table = 'paises_departamentos'
        unique_together = (('id_departamento_pais', 'id_pais'),)
        app_label = 'api'


class PqrRegistros(models.Model):
    id_pqr_registro = models.BigAutoField(primary_key=True)
    id_prq_tipo = models.ForeignKey('PqrTipos', on_delete=models.CASCADE, db_column='id_prq_tipo')
    id_usuario_pqr = models.ForeignKey('Usuarios', on_delete=models.CASCADE, db_column='id_usuario_pqr', related_name='id_usuario_pqr_registros')
    pqr_texto = models.TextField(blank=True, null=True)
    pqr_fechaenvio = models.DateTimeField()
    pqr_respuesta = models.TextField(blank=True, null=True)
    pqr_fecharespuesta = models.DateTimeField(blank=True, null=True)
    id_usuario_respuesta = models.ForeignKey('Usuarios', on_delete=models.CASCADE, db_column='id_usuario_respuesta', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pqr_registros'
        app_label = 'api'


class PqrTipos(models.Model):
    id_prq_tipo = models.AutoField(primary_key=True)
    pq_tipo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pqr_tipos'
        app_label = 'api'


class Usuarios(models.Model):
    id_usuario = models.UUIDField(primary_key=True)
    id_cliente_internal = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente_internal')
    id_tipo_usuario = models.ForeignKey('UsuariosTipos', models.DO_NOTHING, db_column='id_tipo_usuario')
    nombre_usuario = models.CharField(max_length=254)
    id_tipo_documento = models.ForeignKey(DocumentosTipos, models.DO_NOTHING, db_column='id_tipo_documento', blank=True, null=True)
    numero_documento = models.BigIntegerField(blank=True, null=True)
    email_usuario = models.CharField(max_length=254, blank=True, null=True)
    celular_usuario = models.CharField(max_length=15, blank=True, null=True)
    usuario_bloqueado = models.BooleanField(blank=True, null=True)
    usuario_activo = models.BooleanField(blank=True, null=True)
    acceso_plataforma = models.BooleanField(blank=True, null=True)
    usuario_creado_por = models.UUIDField()
    fechahora_creacion_usuario = models.DateTimeField()
    fechahora_ultima_edicion = models.DateTimeField()
    id_usuario_publico = models.BigIntegerField(unique=True)
    recibir_comm = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios'
        app_label = 'api'


class UsuariosAccesosDispositivos(models.Model):
    id_usuario = models.OneToOneField(Usuarios, on_delete=models.CASCADE, db_column='id_usuario', related_name='id_usuario_acceso', primary_key=True)
    id_dispositivo = models.ForeignKey(Dispositivos, on_delete=models.CASCADE, db_column='id_dispositivo')
    can_read = models.BooleanField()
    can_write = models.BooleanField()
    acceso_tercero = models.BooleanField()
    usuario_otorgante_acceso = models.ForeignKey(Usuarios, on_delete=models.CASCADE, db_column='usuario_otorgante_acceso')
    fechahora_permiso = models.DateTimeField(blank=True, null=True)
    recibir_notificacion_mssg_texto = models.BooleanField()
    recibir_notificacion_voice = models.BooleanField()
    fechahora_ultimaconsulta = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios_accesos_dispositivos'
        unique_together = (('id_usuario', 'id_dispositivo'),)
        app_label = 'api'


class UsuariosComunicacion(models.Model):
    id_comm_medio_interno = models.AutoField(primary_key=True)
    id_comm_tipo_medio = models.ForeignKey(ComunicacionesMedios, models.DO_NOTHING, db_column='id_comm_tipo_medio')
    id_prop_medio = models.CharField(max_length=100)
    id_usuario = models.ForeignKey(Usuarios, models.DO_NOTHING, db_column='id_usuario', blank=True, null=True)
    username_chat_usuario = models.CharField(max_length=200, blank=True, null=True)
    fechahora_registro = models.DateTimeField(blank=True, null=True)
    celular_usuario_medio = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuarios_comunicacion'
        app_label = 'api'

class personalizadoBaseUserManager(BaseUserManager):
    def create_user(self, login_celular, password):
        user = self.model(login_celular=login_celular)
        user.set_password(password)
        id_user = Usuarios.objects.get(celular_usuario=login_celular)
        user.id_usuario = id_user.id_usuario
        user.is_active = True
        user.is_staff = False
        user.is_superuser = False
        user.reset_password = True
        user.save()
        return user 

def create_superuser(self, login_celular, password):
        user = self.create_user(login_celular, password)
        id_user = Usuarios.objects.get(celular_usuario=login_celular)
        user.id_usuario = id_user
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.reset_password = True
        user.save()
        return user


class UsuariosLogins(models.Model):
    id_usuario = models.OneToOneField(Usuarios, on_delete=models.CASCADE, db_column='id_usuario', primary_key=True)
    login_celular = models.CharField(unique=True, max_length=15)
    password = models.TextField()
    is_active = models.BooleanField()
    is_staff = models.BooleanField()
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    reset_password = models.BooleanField()
    fecha_expr_passwd = models.DateTimeField(blank=True, null=True)
    fechahora_registro = models.DateTimeField(blank=True, null=True)
    USERNAME_FIELD = 'login_celular'
    REQUIRED_FIELDS = []

    objects = personalizadoBaseUserManager()

    class Meta:
        managed = False
        db_table = 'usuarios_logins'
        app_label = 'api'


class UsuariosTipos(models.Model):
    id_usuario_tipo = models.AutoField(primary_key=True)
    tipo_usuario = models.CharField(max_length=50)
    usuario_dt2 = models.BooleanField()
    superuser = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'usuarios_tipos'
        app_label = 'api'
