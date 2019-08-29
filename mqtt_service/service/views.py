from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import json
import paho.mqtt.client as mqtt
import ssl 
from service import models
import re
import os
from os import environ
from rest_framework.response import Response
from rest_framework import status
import yaml
configpath = os.path.join('./config', 'config.yml')
config = yaml.safe_load(open(configpath))
# Create your views here.

@permission_classes((AllowAny,))
@api_view(['POST'])
def controles(request):
    if request.method == 'POST':
        data = request.data
        # print(config['MQTT_USER']+ " " + config['MQTT_PASSWD']+ " " + config['BROKER_MQTT_HOST']) 
        dispositivo = data['dispositivo']
        puerto = data['puerto']
        estado = data['estado']
        topic = models.Dispositivos.objects.filter(id_dispositivo=dispositivo).values('id_mqtt')
        topic = topic[0]
        rele = re.split("[REL0 ]+", puerto)
        rele = list(filter(None, rele))
        usr = data['cel_user']
        id_usr = models.Usuarios.objects.get(celular_usuario=usr)
        id_usr_ref = models.DispositivosUsuariosReferenciaCliente.objects.get(id_usuario=id_usr.id_usuario, id_dispositivo=dispositivo)
        id_usr_ref = str(id_usr_ref.id_dispositivo_usuario_referencia_cliente)
        if estado is True:
            OnOff = '1'
        elif estado is False:
            OnOff = '0'
        comandJson = json.dumps({'CMX': '12', 'RL'+rele[0]: OnOff, 'U': id_usr_ref}, sort_keys=True, separators=(',', ':'))
        try:
            client = mqtt.Client(client_id="1", clean_session=True, userdata=None, protocol=mqtt.MQTTv31, transport="tcp")

            TLS_CERT_PATH = 'certs/ca.pem'
            key = 'certs/client.key'
            cc = 'certs/client.crt'
            

            client.username_pw_set(config['MQTT_USER'], config['MQTT_PASSWD'])

            client.tls_set(ca_certs=TLS_CERT_PATH, certfile=cc, keyfile=key, cert_reqs=ssl.CERT_REQUIRED, tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
            client.tls_insecure_set(False)
            client.connect(config['BROKER_MQTT_HOST'], 1884, 60)

            client.publish("m1/dt/"+topic['id_mqtt']+"/in/", comandJson)

        except Exception:
                print("no se pudo conectar con el MQTT Broker...")
                return Response({'ERROR': 'CONTROLS'}, status=status.HTTP_400_BAD_REQUEST)
    return Response({'OK': 'CONTROLS'}, status=status.HTTP_201_CREATED)
