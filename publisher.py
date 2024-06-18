import paho.mqtt.client as mqtt

broker_address = "localhost"
topic = "test/topic"

client = mqtt.Client("Publisher")
client.connect(broker_address)
client.loop_start()
count = 0
while count < 1000:
    client.publish(topic, "Hello, MQTT!!!!")
    print("Message Sent! {}".format(count))
    count += 1
client.loop_stop()
client.disconnect()