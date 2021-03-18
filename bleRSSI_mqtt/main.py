import time
import paho.mqtt.client as mqtt
from pysinewave import SineWave

sinewave = SineWave(pitch = 12, pitch_per_second = 10)

def process_message(client, userdata, message):
    bericht = str(message.payload.decode("utf-8"))
    gesplitst = bericht.split("_")
    RSSI = gesplitst[0]
    print(bericht)
    if (float(RSSI) > -30):
        sinewave.play()
        time.sleep(1)
        sinewave.stop()

# Create client
client = mqtt.Client(client_id="subscriber-1")

# Assign callback function
client.on_message = process_message

# Connect to broker
client.connect("192.168.43.101",1883,60)

# Subscriber to topic
client.subscribe("esp32/afstand/rssi")

# Run loop
client.loop_forever()