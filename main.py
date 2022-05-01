from decouple import config
import paho.mqtt.client as mqtt
from Door import Door

door = Door(
    int(config("MOTOR_PIN1")), 
    int(config("MOTOR_PIN2")), 
    10
)

def on_connect(client, userdata, flags, rc):
    print("Connected with code " + str(rc))
    client.subscribe(config("CHANNEL"))

def on_message(client, userdata, msg):
    print("Topic: " + str(msg.topic))
    print("Message: " + str(msg.payload))
    print("---")

    door.handle(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.username_pw_set(str(config("MQTT_USER")), str(config("MQTT_PASSWORD")))

client.connect(config("HOST"), int(config("PORT")), 60)

client.loop_forever()