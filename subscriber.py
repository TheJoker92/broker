import paho.mqtt.client as mqtt

broker_address = "localhost"
topic = "test/topic"

def on_message(client, userdata, message):
    print("Message received: ", str(message.payload.decode("utf-8")))

client = mqtt.Client("Subscriber")
client.on_message = on_message

client.connect(broker_address)
client.subscribe(topic)
client.loop_forever()
