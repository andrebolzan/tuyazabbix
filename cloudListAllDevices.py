import argparse
import tinytuya # pip install tinytuya
from tabulate import tabulate #pip install tabulate

# Configurar o argparse para receber os parâmetros via linha de comando
parser = argparse.ArgumentParser(description='Obtenha o status de um dispositivo Tuya.')

# Definindo os argumentos que o script aceitará
parser.add_argument('apikey', type=str, help='key da API Tuya')
parser.add_argument('apiSecret', type=str, help='Secret da API')

# Analisa os argumentos fornecidos via linha de comando
args = parser.parse_args()

# Connect to Tuya Cloud
c = tinytuya.Cloud(
    apiRegion="us",
    apiKey=args.apikey,  # Corrigido: adicionada vírgula
    apiSecret=args.apiSecret
)

# Display list of devices
devices = c.getdevices()

# Seleciona as colunas que deseja exibir
headers = ["name", "id", "key", "mac", "category", "product_name", "model"]

# Prepara a lista de dispositivos com os campos desejados
device_list = [[device.get(header, '') for header in headers] for device in devices]

# Ordena a lista pela coluna "name" (primeiro campo em cada sublista)
device_list_sorted = sorted(device_list, key=lambda x: x[0])

# Exibe a tabela ordenada
print(tabulate(device_list_sorted, headers=headers, tablefmt="grid"))
