from flask.json import jsonify
import paho.mqtt.client as mqtt
import json
import datetime

data1 = 100
data2 = 0
data3 = 100

MQTT_Topic_Switch = "CyberLink/commands/1037600"
MQTT_Broker = "localhost"
MQTT_Port = 1883
Keep_Alive_Interval = 45


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
		
def send_data_to_switch(data):
	mqttc = mqtt.Client()
	mqttc.on_connect = on_connect
	mqttc.on_disconnect = on_disconnect
	mqttc.on_publish = on_publish
	mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))
	switchData = {
	 	"id":"1037600",
	 	"data":{
	 		"out1": int(data['out1']),
	 		"out2": int(data['out2']),
	 		"out3": int(data['out3'])
	 	}
	}
	print(switchData)
	dataJson = json.dumps(switchData)
	mqttc.publish("CyberLink/commands/1037600", dataJson)
	save_switch_state(data)
	response_object = {
		'status': 'success',
	}
	return response_object, 401
    
def save_switch_state(data):
	global data1, data2, data3
	data1 = data['out1']
	data2 = data['out2']
	data3 = data['out3']

def get_last_state():
	last_state = jsonify(
		out1 = int(data1),
		out2 = int(data2),
		out3 = int(data3)
	)
	return last_state




