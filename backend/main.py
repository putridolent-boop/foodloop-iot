import json
import os

import paho.mqtt.client as mqtt
from dotenv import load_dotenv

from processing import process_temperature

load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER", "broker.hivemq.com")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))

TOPIC_SENSOR = "foodloop/sensor/temperature"
TOPIC_STATUS = "foodloop/status/temperature"


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        print("FoodLoop berhasil terhubung ke MQTT!")
        client.subscribe(TOPIC_SENSOR)
        print("Menunggu data sensor...")
    else:
        print("Koneksi MQTT gagal:", reason_code)


def on_message(client, userdata, message):
    try:
        raw_data = message.payload.decode("utf-8")
        data = json.loads(raw_data)

        result = process_temperature(data.get("temperature"))

        output = {
            "temperature": result["temperature"],
            "status": result["status"],
            "source": "FoodLoop IoT"
        }

        output_json = json.dumps(output)
        print("Data sensor:", output_json)

        client.publish(TOPIC_STATUS, output_json)

    except (UnicodeDecodeError, json.JSONDecodeError, TypeError) as error:
        print("Data sensor tidak valid:", error)


def main():
    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
        client_id="foodloop-backend"
    )

    client.on_connect = on_connect
    client.on_message = on_message

    print("Menghubungkan ke broker MQTT...")

    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.loop_forever()
    except OSError as error:
        print("Gagal terhubung ke MQTT:", error)


if __name__ == "__main__":
    main()
