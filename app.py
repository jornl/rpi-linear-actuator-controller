from decouple import config
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with code" + str(rc))
    client.subscribe(config("CHANNEL"))

def on_message(client, userdata, msg):
    print("Topic: " + str(msg.topic))
    print("Message: " + str(msg.payload))
    print("---")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(config("HOST"), int(config("PORT")), 60)

client.loop_forever()