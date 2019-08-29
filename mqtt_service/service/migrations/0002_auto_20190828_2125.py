# Generated by Django 2.2.2 on 2019-08-28 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Clientes',
        ),
        migrations.DeleteModel(
            name='ClientesContactos',
        ),
        migrations.DeleteModel(
            name='ClientesContactosTipos',
        ),
        migrations.RemoveField(
            model_name='clientesdispositivos',
            name='id_dispositivo',
        ),
        migrations.DeleteModel(
            name='ComunicacionesEstrategias',
        ),
        migrations.DeleteModel(
            name='ComunicacionesMedios',
        ),
        migrations.DeleteModel(
            name='ComunicacionesMssgsEnviadas',
        ),
        migrations.RemoveField(
            model_name='comunicacionesnotificaciones',
            name='id_notificacion',
        ),
        migrations.DeleteModel(
            name='DispositivosLotes',
        ),
        migrations.DeleteModel(
            name='DispositivosModelos',
        ),
        migrations.DeleteModel(
            name='DispositivosModelosPuertosBasicos',
        ),
        migrations.DeleteModel(
            name='DispositivosNotificaciones',
        ),
        migrations.DeleteModel(
            name='DispositivosPuertos',
        ),
        migrations.DeleteModel(
            name='DispositivosPuertosModelosTipos',
        ),
        migrations.DeleteModel(
            name='DispositivosTipos',
        ),
        migrations.DeleteModel(
            name='DispositivosUbicaciones',
        ),
        migrations.RemoveField(
            model_name='dispositivosusuariosreferenciacliente',
            name='id_dispositivo',
        ),
        migrations.DeleteModel(
            name='DispositivosUsuariosSinReferencia',
        ),
        migrations.DeleteModel(
            name='DocumentosTipos',
        ),
        migrations.DeleteModel(
            name='NotificacionesAlertaNiveles',
        ),
        migrations.DeleteModel(
            name='NotificacionesTipos',
        ),
        migrations.DeleteModel(
            name='OperadoresCelulares',
        ),
        migrations.DeleteModel(
            name='OperadoresCelularesPlanesDatos',
        ),
        migrations.DeleteModel(
            name='OperadoresCelularesSimCards',
        ),
        migrations.DeleteModel(
            name='Paises',
        ),
        migrations.DeleteModel(
            name='PaisesCiudades',
        ),
        migrations.DeleteModel(
            name='PaisesDepartamentos',
        ),
        migrations.DeleteModel(
            name='PqrRegistros',
        ),
        migrations.DeleteModel(
            name='PqrTipos',
        ),
        migrations.RemoveField(
            model_name='usuariosaccesosdispositivos',
            name='id_usuario',
        ),
        migrations.DeleteModel(
            name='UsuariosComunicacion',
        ),
        migrations.RemoveField(
            model_name='usuarioslogins',
            name='id_usuario',
        ),
        migrations.DeleteModel(
            name='UsuariosTipos',
        ),
        migrations.DeleteModel(
            name='ClientesDispositivos',
        ),
        migrations.DeleteModel(
            name='ComunicacionesNotificaciones',
        ),
        migrations.DeleteModel(
            name='Dispositivos',
        ),
        migrations.DeleteModel(
            name='DispositivosUsuariosReferenciaCliente',
        ),
        migrations.DeleteModel(
            name='Notificaciones',
        ),
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.DeleteModel(
            name='UsuariosAccesosDispositivos',
        ),
        migrations.DeleteModel(
            name='UsuariosLogins',
        ),
    ]
