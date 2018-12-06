from __future__ import print_function
from database import Database
from models import Muestras

import random
import time
import paho.mqtt.client as mqtt

import sys
#def main es el metodo donde se generan los datos aleatorios de la estacion meteorologica de la ciudad de buenos aires
#la estacion climatica sobre la cual simulamos es la de invierno
broker = "10.0.2.15"
pasos=0
db=None
session=None
 
class GracefulKiller:
    kill_now = False
    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, signum, frame):
        self.kill_now = True


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(mqttc, obj, msg):
    global session
    global samples
    pasos = msg.payload 
    distancia = msg.payload 
    calorias = msg.payload 
    velocidad = msg.payload
    muestras=Muestras(pasos,distancia,calorias,velocidad) 
    session.add(muestras)
    session.commit()
    if killer.kill_now:
        session.close()
        #break
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

def main ():
  global db
  global session
  global samples
  db = Database()
  session = db.get_session()
  mqttc = mqtt.Client()
  mqttc.connect(broker,1883, 60)
  mqttc.subscribe("/pasos", 0)
  mqttc.on_subscribe = on_subscribe
  mqttc.on_message = on_message
  mqttc.loop_forever()


if __name__ == '__main__':
  main()
  