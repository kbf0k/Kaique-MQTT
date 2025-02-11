# MQTT Publisher & Subscriber

Este repositório contém dois scripts em Python que utilizam a biblioteca `paho-mqtt` para comunicação via protocolo MQTT.

## 📌 Descrição

Os scripts implementam um **Subscriber** e um **Publisher** que se comunicam através do broker público **HiveMQ** no tópico `senai/dev`.

- O **Subscriber** (`mqtt_subscriber.py`) se conecta ao broker, escuta o tópico e exibe mensagens recebidas.
- O **Publisher** (`mqtt_publisher.py`) permite que o usuário envie mensagens para o tópico via entrada do teclado.

## 📂 Estrutura dos Arquivos

- `mqtt_subscriber.py` → Script que recebe mensagens do tópico MQTT.
- `mqtt_publisher.py` → Script que publica mensagens no tópico MQTT.

## ⚙️ Configuração

### 📌 Requisitos

Certifique-se de ter o Python instalado e a biblioteca `paho-mqtt`:

```bash
pip install paho-mqtt
```

### 📡 Uso

#### 1️⃣ Iniciar o Subscriber

Execute o script para escutar mensagens no tópico:

```bash
python mqtt_subscriber.py
```

#### 2️⃣ Iniciar o Publisher

Em outro terminal, execute:

```bash
python mqtt_publisher.py
```

Digite mensagens e pressione **Enter** para enviá-las ao tópico MQTT.

## 📢 Exemplo de Funcionamento

**No Subscriber:**

```
Inscrito no tópico 'senai/dev', aguardando mensagens...
Mensagem recebida no tópico 'senai/dev': Olá, MQTT!
```

**No Publisher:**

```
Digite uma mensagem para enviar: Olá, MQTT!
Mensagem 'Olá, MQTT!' publicada no tópico 'senai/dev'
```

## 📖 Referências

- [Documentação do Paho MQTT](https://www.eclipse.org/paho/)
- [Broker Público HiveMQ](https://www.hivemq.com/public-mqtt-broker/)
