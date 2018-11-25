from __future__ import print_function
from database import Database
from models import Samples

import random
import time
import paho.mqtt.client as mqtt

import sys
#def main es el metodo donde se generan los datos aleatorios de la estacion meteorologica de la ciudad de buenos aires
#la estacion climatica sobre la cual simulamos es la de invierno
broker = "192.168.0.120"
pasos=0
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(mqttc, obj, msg):
    global session
    global samples
    samples.pasos = msg.payload 
    samples.distancia = msg.payload 
    samples.calorias = msg.payload 
    samples.velocidad = msg.payload 
    session.add(samples)
    session.commit()
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))

#def main (Samples, session): 
 #   global flag
  #  s = Samples            
   # while(True):
    #    if flag == True:
     #       s.pasos = pasos
      #      flag = False
       #     session.add(s)
        #    session.commit()
        #time.sleep(1)
    #session.close()
 
################################################################################
#if __name__ == '__main__':
#    db = Database()
#    session = db.get_session()
#    samples = Samples()
#    mqttc = mqtt.Client()
#    mqttc.connect(broker, 1883, 60)
#    mqttc.subscribe("/pasos", 0)
#    mqttc.on_subscribe = on_subscribe
#    mqttc.on_message = on_message
#    main(samples, session)
db = Database()
session = db.get_session()
samples = Samples()
mqttc = mqtt.Client()
mqttc.connect(broker, 1883, 60)
mqttc.subscribe("/pasos", 0)
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message

mqttc.loop_forever()