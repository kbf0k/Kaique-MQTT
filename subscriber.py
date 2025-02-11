import paho.mqtt.client as mqtt

broker = "broker.hivemq.com"
port = 1883
topic = "senai/dev"

# Unidade Curricular - Redes IoT
# Aula 1: MQTT - Prof. Wesley Fioreze

def on_message(client, userdata, msg):
    print(f"Mensagem recebida no tópico '{msg.topic}': {msg.payload.decode()}")

client = mqtt.Client()
client.on_message = on_message
client.connect(broker, port)

client.subscribe(topic)
print(f"Inscrito no tópico '{topic}', aguardando mensagens...")

client.loop_forever()