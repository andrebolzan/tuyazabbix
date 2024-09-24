#!/usr/bin/env python3
import argparse
import tinytuya  # pip install tinytuya
from tabulate import tabulate  # pip install tabulate

# Configurar o argparse para receber os parâmetros via linha de comando
parser = argparse.ArgumentParser(description='Obtenha o status de um dispositivo Tuya.')

# Definindo os argumentos que o script aceitará
parser.add_argument('apikey', type=str, help='key da API Tuya')
parser.add_argument('apiSecret', type=str, help='Secret da API')
parser.add_argument('--geralocalkey', action='store_true', help='Gera um arquivo localKey.txt com id e key (opcional)')

# Analisa os argumentos fornecidos via linha de comando
args = parser.parse_args()

# Connect to Tuya Cloud
c = tinytuya.Cloud(
    apiRegion="us",
    apiKey=args.apikey,
    apiSecret=args.apiSecret
)

# Display list of devices
devices = c.getdevices()

# Seleciona os campos desejados
keys = ["id", "key"]
local_keys = []

# Coleta os id's e keys dos dispositivos
for device in devices:
    device_id = device.get("id")
    device_key = device.get("key")
    if device_id and device_key:
        local_keys.append(f"{device_id}|{device_key}")

# Se o parâmetro geralocalkey for passado, gera o arquivo localKey.txt
if args.geralocalkey:
    with open('localKey.txt', 'w') as f:
        for local_key in local_keys:
            f.write(local_key + '\n')
    print("Arquivo localKey.txt gerado com sucesso.")
else:
    # Exibe a tabela de dispositivos
    headers = ["name", "id", "key", "mac", "category", "product_name", "model"]
    device_list = [[device.get(header, '') for header in headers] for device in devices]
    device_list_sorted = sorted(device_list, key=lambda x: x[0])
    print(tabulate(device_list_sorted, headers=headers, tablefmt="grid"))
