# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import json

# MQTT Settings 
MQTT_Broker = "localhost"
#MQTT_Broker = "mqtt.iotwithus.com"
MQTT_Port = 1883
Keep_Alive_Interval = 45
MQTT_Topic_Switch = "CyberLink/commands/1037600"

def on_connect(client, userdata, rc,  properties=None):
	if rc != 0:
		print("Unable to connect to MQTT Broker...")
	else:
		print("Connected with MQTT Broker: " + str(MQTT_Broker))

def on_publish(client, userdata, mid):
	pass
		
def on_disconnect(client, userdata, rc):
	if rc !=0:
		print("pass")
		
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_disconnect = on_disconnect
mqttc.on_publish = on_publish

mqttc.username_pw_set(username="username",password="@Iot123456")
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))		

		
def publish_To_Topic(topic, message):
	mqttc.publish(topic,message)
	print("Published: " + str(message) + " " + "on MQTT Topic: " + str(topic))
	print("")

def publish_data_to_switch(data1, data2, data3):
	switchData = {
	 	"id":"1037600",
	 	"data":{
	 		"out1": data1,
	 		"out2": data2,
	 		"out3": data3
	 	}
	}
	switchDataJson = json.dumps(switchData)
	publish_To_Topic ("CyberLink/commands/1037600", switchDataJson)
	
publish_data_to_switch(0, 100, 0)

