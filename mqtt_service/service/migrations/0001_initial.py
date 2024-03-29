# Generated by Django 2.2.2 on 2019-08-28 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id_cliente_internal', models.BigIntegerField(primary_key=True, serialize=False)),
                ('id_cliente_uuid', models.UUIDField()),
                ('id_cliente_external', models.IntegerField()),
                ('id_documentos_tipos', models.IntegerField()),
                ('numero_documento', models.BigIntegerField()),
                ('nombre_cliente', models.CharField(max_length=255)),
                ('direccion_principal', models.CharField(max_length=255)),
                ('id_ciudad', models.IntegerField()),
                ('id_departamento', models.IntegerField()),
                ('id_pais', models.IntegerField()),
                ('comentarios_cliente', models.TextField(blank=True, null=True)),
                ('cliente_bloqueado', models.BooleanField(blank=True, null=True)),
                ('cliente_activo', models.BooleanField(blank=True, null=True)),
                ('fecha_no_activo', models.DateField(blank=True, null=True)),
                ('fechahora_registro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clientes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientesContactos',
            fields=[
                ('id_cliente_contacto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_contacto', models.CharField(blank=True, max_length=100, null=True)),
                ('telefono_fijo_contacto', models.CharField(blank=True, max_length=15, null=True)),
                ('celular_contacto', models.CharField(blank=True, max_length=15, null=True)),
                ('email_contacto', models.CharField(blank=True, max_length=254, null=True)),
                ('detalles_contacto', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clientes_contactos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientesContactosTipos',
            fields=[
                ('id_cliente_contacto_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_contacto', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'clientes_contactos_tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ComunicacionesEstrategias',
            fields=[
                ('id_comunicacion_estrategia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_estrategia', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'comunicaciones_estrategias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ComunicacionesMedios',
            fields=[
                ('id_comunicacion_medio', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_medio', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'comunicaciones_medios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ComunicacionesMssgsEnviadas',
            fields=[
                ('id_comm_mssg_enviada', models.BigIntegerField(primary_key=True, serialize=False)),
                ('mssg_enviada', models.TextField(blank=True, null=True)),
                ('mssg_enviada_fechahora', models.DateTimeField()),
                ('time_utc_epc_pub', models.FloatField(blank=True, null=True)),
                ('time_utc_epc_mssg_enviada', models.FloatField(blank=True, null=True)),
                ('id_dispositivos_notificaciones', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'comunicaciones_mssgs_enviadas',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Dispositivos',
            fields=[
                ('id_dispositivo', models.BigIntegerField(primary_key=True, serialize=False)),
                ('numero_serie', models.CharField(max_length=20, unique=True)),
                ('id_mqtt', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('imei', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('status_inicializado', models.BooleanField(blank=True, null=True)),
                ('status_dispositivo', models.BooleanField(blank=True, null=True)),
                ('fechahora_activacion', models.DateTimeField(blank=True, null=True)),
                ('fechahora_registro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dispositivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispositivosLotes',
            fields=[
                ('id_dispositivo_lote', models.AutoField(primary_key=True, serialize=False)),
                ('codigo_lote', models.CharField(blank=True, max_length=5, null=True)),
                ('unidades_lote', models.IntegerField()),
                ('fecha_inicial_fabr_lote', models.DateField()),
                ('fecha_final_fabr_lote', models.DateField(blank=True, null=True)),
                ('detalles_lote', models.TextField(blank=True, null=True)),
                ('fechahora_registro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dispositivos_lotes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispositivosModelos',
            fields=[
                ('id_dispositivo_modelo_internal', models.AutoField(primary_key=True, serialize=False)),
                ('id_dispositivo_modelo_external', models.CharField(max_length=5)),
                ('nombre_modelo', models.CharField(blank=True, max_length=20, null=True)),
                ('version_hardware_dispositivo', models.CharField(max_length=10)),
                ('version_software_dispositivo', models.CharField(max_length=10)),
                ('detalles_dispositivo', models.TextField(blank=True, null=True)),
                ('fechahora_registro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dispositivos_modelos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispositivosModelosPuertosBasicos',
            fields=[
                ('id_dispositivo_modelo', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('id_modelo_puerto', models.IntegerField()),
                ('cantidad_puertos', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'dispositivos_modelos_puertos_basicos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispositivosNotificaciones',
            fields=[
                ('id_dispositivos_notificaciones', models.BigIntegerField(primary_key=True, serialize=False)),
                ('id_mssg_mqtt', models.BigIntegerField()),
                ('valor_medida_notificacion', models.FloatField(blank=True, null=True)),
                ('time_utc_pub', models.DateTimeField()),
                ('time_utc_epc_pub', models.FloatField()),
                ('time_utc_epc_load', models.FloatField()),
                ('comm_prcssd', models.BooleanField()),
                ('time_utc_comm_prcssd', models.DateTimeField(blank=True, null=True)),
                ('time_utc_epc_comm_prcssd', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dispositivos_notificaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispositivosPuertos',
            fields=[
                ('id_dispositivo_puerto', models.AutoField(primary_key=True, serialize=False)),
                ('cod_puerto_dispo', models.CharField(max_length=5)),
                ('nombre_puerto', models.CharField(max_length=50)),
                ('descripcion_puerto', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dispositivos_puertos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispositivosPuertosModelosTipos',
            fields=[
                ('id_modelo_puerto', models.AutoField(primary_key=True, serialize=False)),
                ('modelo_puerto_codigo', models.CharField(blank=True, max_length=5, null=True)),
                ('modelo_puerto_nombre', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'dispositivos_puertos_modelos_tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispositivosTipos',
            fields=[
                ('id_dispositivo_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_dispositivo', models.CharField(max_length=50, unique=True)),
                ('fechahora_registro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dispositivos_tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispositivosUbicaciones',
            fields=[
                ('id_dispositivo_ubicacion', models.AutoField(primary_key=True, serialize=False)),
                ('cod_ubicacion_nivel1', models.SmallIntegerField()),
                ('cod_ubicacion_nivel2', models.SmallIntegerField()),
                ('nombre_corto_ubicacion_nivel1', models.CharField(blank=True, max_length=50, null=True)),
                ('nombre_corto_ubicacion_nivel2', models.CharField(blank=True, max_length=50, null=True)),
                ('detalle_ubicacion', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dispositivos_ubicaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispositivosUsuariosSinReferencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_dispositivo_usuario_referencia_cliente', models.IntegerField(blank=True, null=True)),
                ('time_utc_pub', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'dispositivos_usuarios_sin_referencia',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentosTipos',
            fields=[
                ('id_documentos_tipos', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_documento', models.CharField(max_length=30)),
                ('documento_persona_natural', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'documentos_tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Notificaciones',
            fields=[
                ('id_notificacion', models.IntegerField(primary_key=True, serialize=False)),
                ('cod_notificacion', models.CharField(max_length=5)),
                ('nombre_notificacion', models.CharField(max_length=50)),
                ('detalle_notificacion', models.CharField(blank=True, max_length=200, null=True)),
                ('notificacion_icon_front', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'notificaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificacionesAlertaNiveles',
            fields=[
                ('id_alerta_nivel', models.IntegerField(primary_key=True, serialize=False)),
                ('alerta_nivel_severidad', models.CharField(blank=True, max_length=30, null=True)),
                ('alerta_nivel_informacion', models.CharField(blank=True, max_length=30, null=True)),
                ('alerta_nivel_color', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'notificaciones_alerta_niveles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='NotificacionesTipos',
            fields=[
                ('id_tipo_notificacion', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_notificacion', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'db_table': 'notificaciones_tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OperadoresCelulares',
            fields=[
                ('id_operador_celular', models.AutoField(primary_key=True, serialize=False)),
                ('operador_celular', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'operadores_celulares',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OperadoresCelularesPlanesDatos',
            fields=[
                ('id_plan_datos', models.SmallIntegerField(primary_key=True, serialize=False)),
                ('plan_datos_nombre', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'operadores_celulares_planes_datos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OperadoresCelularesSimCards',
            fields=[
                ('id_sim_card', models.AutoField(primary_key=True, serialize=False)),
                ('id_serial_sim', models.BigIntegerField(blank=True, null=True)),
                ('numero_celular', models.CharField(max_length=15, unique=True)),
            ],
            options={
                'db_table': 'operadores_celulares_sim_cards',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Paises',
            fields=[
                ('id_pais', models.AutoField(primary_key=True, serialize=False)),
                ('iso', models.CharField(max_length=2)),
                ('nombre_pais_iso', models.CharField(max_length=80)),
                ('nombre_pais_esp', models.CharField(blank=True, max_length=80, null=True)),
                ('nombre_pais_ing', models.CharField(max_length=80)),
                ('iso3', models.CharField(blank=True, max_length=3, null=True)),
                ('numcode', models.SmallIntegerField(blank=True, null=True)),
                ('phonecode', models.SmallIntegerField()),
                ('active', models.BooleanField()),
            ],
            options={
                'db_table': 'paises',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaisesCiudades',
            fields=[
                ('id_ciudad', models.AutoField(primary_key=True, serialize=False)),
                ('cod_ciudad_pais', models.CharField(blank=True, max_length=20, null=True)),
                ('id_departamento_pais', models.SmallIntegerField(blank=True, null=True)),
                ('nombre_ciudad', models.CharField(max_length=100)),
                ('region_ciudad', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'paises_ciudades',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PaisesDepartamentos',
            fields=[
                ('id_departamento', models.AutoField(primary_key=True, serialize=False)),
                ('id_departamento_pais', models.SmallIntegerField()),
                ('departamento', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'paises_departamentos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PqrRegistros',
            fields=[
                ('id_pqr_registro', models.BigAutoField(primary_key=True, serialize=False)),
                ('pqr_texto', models.TextField(blank=True, null=True)),
                ('pqr_fechaenvio', models.DateTimeField()),
                ('pqr_respuesta', models.TextField(blank=True, null=True)),
                ('pqr_fecharespuesta', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pqr_registros',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PqrTipos',
            fields=[
                ('id_prq_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('pq_tipo', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'pqr_tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.UUIDField(primary_key=True, serialize=False)),
                ('nombre_usuario', models.CharField(max_length=254)),
                ('numero_documento', models.BigIntegerField(blank=True, null=True)),
                ('email_usuario', models.CharField(blank=True, max_length=254, null=True)),
                ('celular_usuario', models.CharField(blank=True, max_length=15, null=True)),
                ('usuario_bloqueado', models.BooleanField(blank=True, null=True)),
                ('usuario_activo', models.BooleanField(blank=True, null=True)),
                ('acceso_plataforma', models.BooleanField(blank=True, null=True)),
                ('usuario_creado_por', models.UUIDField()),
                ('fechahora_creacion_usuario', models.DateTimeField()),
                ('fechahora_ultima_edicion', models.DateTimeField()),
                ('id_usuario_publico', models.BigIntegerField(unique=True)),
                ('recibir_comm', models.BooleanField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuarios',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuariosComunicacion',
            fields=[
                ('id_comm_medio_interno', models.AutoField(primary_key=True, serialize=False)),
                ('id_prop_medio', models.CharField(max_length=100)),
                ('username_chat_usuario', models.CharField(blank=True, max_length=200, null=True)),
                ('fechahora_registro', models.DateTimeField(blank=True, null=True)),
                ('celular_usuario_medio', models.CharField(blank=True, max_length=15, null=True)),
            ],
            options={
                'db_table': 'usuarios_comunicacion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuariosTipos',
            fields=[
                ('id_usuario_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_usuario', models.CharField(max_length=50)),
                ('usuario_dt2', models.BooleanField()),
                ('superuser', models.BooleanField()),
            ],
            options={
                'db_table': 'usuarios_tipos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ClientesDispositivos',
            fields=[
                ('id_dispositivo', models.ForeignKey(db_column='id_dispositivo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='service.Dispositivos')),
                ('nombre_corto_cliente_dispositivo', models.CharField(blank=True, max_length=50, null=True)),
                ('localizacion_cliente_dispositivo', models.CharField(blank=True, max_length=50, null=True)),
                ('detalle_dispositivo', models.TextField(blank=True, null=True)),
                ('fechahora_registro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'clientes_dispositivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ComunicacionesNotificaciones',
            fields=[
                ('id_notificacion', models.ForeignKey(db_column='id_notificacion', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='service.Notificaciones')),
            ],
            options={
                'db_table': 'comunicaciones_notificaciones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DispositivosUsuariosReferenciaCliente',
            fields=[
                ('id_dispositivo_usuario_autonumber', models.IntegerField(default=1)),
                ('id_dispositivo', models.ForeignKey(db_column='id_dispositivo', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='service.Dispositivos')),
                ('id_dispositivo_usuario_referencia_cliente', models.IntegerField(blank=True, null=True)),
                ('observacion_dispositivo_usuario', models.TextField(blank=True, null=True)),
                ('usuario_puede_leer_dispositivo', models.BooleanField()),
                ('usuario_puede_editar_dispositivo', models.BooleanField()),
            ],
            options={
                'db_table': 'dispositivos_usuarios_referencia_cliente',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuariosAccesosDispositivos',
            fields=[
                ('id_usuario', models.OneToOneField(db_column='id_usuario', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='id_usuario_acceso', serialize=False, to='service.Usuarios')),
                ('can_read', models.BooleanField()),
                ('can_write', models.BooleanField()),
                ('acceso_tercero', models.BooleanField()),
                ('fechahora_permiso', models.DateTimeField(blank=True, null=True)),
                ('recibir_notificacion_mssg_texto', models.BooleanField()),
                ('recibir_notificacion_voice', models.BooleanField()),
                ('fechahora_ultimaconsulta', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuarios_accesos_dispositivos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UsuariosLogins',
            fields=[
                ('id_usuario', models.ForeignKey(db_column='id_usuario', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='service.Usuarios')),
                ('login_celular', models.CharField(max_length=15, unique=True)),
                ('password', models.TextField()),
                ('is_active', models.BooleanField()),
                ('is_staff', models.BooleanField()),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('reset_password', models.BooleanField()),
                ('fecha_expr_passwd', models.DateTimeField(blank=True, null=True)),
                ('fechahora_registro', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'usuarios_logins',
                'managed': False,
            },
        ),
    ]
