#!/usr/bin/env python3
import argparse
import tinytuya

def get_device_status_cloud(device_id, device_type):
    # Conectar à Tuya Cloud
    c = tinytuya.Cloud(
        apiRegion="us",
        apiKey="4sgpxxqtvhy785s559hr",
        apiSecret="b63a2f1aa92548b6a31eaec8db3893c6"
    )

    # Exibir status do dispositivo
    result = c.getstatus(device_id)
    if result.get('success'):

        #exibir status - Debug
        #print (result)
        if device_type == 'sensor':
            online = c.getconnectstatus(device_id)

            temp = next(item['value'] for item in result['result'] if item['code'] == 'va_temperature')
            umid = next(item['value'] for item in result['result'] if item['code'] == 'va_humidity')
            batt = next(item['value'] for item in result['result'] if item['code'] == 'battery_percentage')

            output = f"online;{online};temp;{temp};umid;{umid};batt;{batt};api;{result.get('success')}"
            print(output)
        elif device_type == 'sensor2':
            online = c.getconnectstatus(device_id)

            temp = next(item['value'] for item in result['result'] if item['code'] == 'va_temperature')
            umid = next(item['value'] for item in result['result'] if item['code'] == 'va_humidity')
            batt = next(item['value'] for item in result['result'] if item['code'] == 'battery_state')

            output = f"online;{online};temp;{temp};umid;{umid};batt;{batt};api;{result.get('success')}"
            print(output)        
        elif device_type == 'smoke':
            online = c.getconnectstatus(device_id)

            SentorStatus = next(item['value'] for item in result['result'] if item['code'] == 'smoke_sensor_status')
            TempoAlarme = next(item['value'] for item in result['result'] if item['code'] == 'temper_alarm')
            batt = next(item['value'] for item in result['result'] if item['code'] == 'battery_percentage')

            output = f"online;{online};SentorStatus;{SentorStatus};TempoAlarme;{TempoAlarme};batt;{batt};api;{result.get('success')}"
            print(output)
        else:
            print(f"Tipo de dispositivo {device_type} não implementado ainda.")
    else:
        print(f"online;0;temp;0;batt;0;api;{result.get('Error')}")

def get_device_status_local(device_id, ipv5, key_local, device_type):
    # Conectar ao dispositivo Tuya local
    d = tinytuya.OutletDevice(device_id, ipv5, key_local)
    d.set_version(3.4)
    d.set_socketRetryLimit(3)  # retry count limit [default 5]
    d.set_socketRetryDelay(3)  # retry delay [default 5]
    d.set_socketTimeout(6)  # set connection timeout in seconds [default 5]

    # Ativar coleta de dados
    status = d.status()

    if device_type == 'power':
        if 'dps' in status:
            amperes = status['dps'].get('18', 'N/A')
            watts = status['dps'].get('19', 'N/A')
            volts = status['dps'].get('20', 'N/A')
            potencia = status['dps'].get('52', 'N/A')

            amperes_formatado = f"{amperes / 1000:.1f}" if amperes != 'N/A' else 'N/A'
            watts_formatado = f"{int(watts / 10)}" if watts != 'N/A' else 'N/A'
            volts_formatado = f"{int(volts / 10)}" if volts != 'N/A' else 'N/A'
            potencia_formatado = f"{int(potencia / 10)}" if potencia != 'N/A' else 'N/A'

            output = f"online;True;amper;{amperes_formatado};watts;{watts_formatado};volts;{volts_formatado};potencia;{potencia_formatado};erro;false"
            print(output)
        else:
            print(f"online;False;amper;0;watts;0;volts;0;potencia;0;erro;Erro de Cadastro IP ou localKey")

    elif device_type == 'zigbee':
        # Aqui você pode adicionar a lógica de coleta para dispositivos Zigbee
        # Exemplo:
        if 'dps' in status:
            # Substitua pelos códigos DPS e lógica que o Zigbee usa
            print("Lógica de coleta Zigbee aqui.")
        else:
            print("Erro ao coletar dados Zigbee.")

    else:
        print(f"Tipo de dispositivo {device_type} não implementado no modo local.")

# Configurar o argparse para receber os parâmetros via linha de comando
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Obtenha o status de um dispositivo Tuya.')
    
    # Argumento para escolher entre cloud ou local
    parser.add_argument('mode', type=str, choices=['cloud', 'local'], help='Modo de operação: cloud ou local')
    parser.add_argument('device_type', type=str, help='Tipo de dispositivo (ex: sensor, power, zigbee)')
    parser.add_argument('device_id', type=str, help='ID do dispositivo Tuya')

    # Argumentos opcionais para o modo local
    parser.add_argument('ipv5', type=str, nargs='?', help='Endereço IP do dispositivo Tuya (para o modo local)')
    parser.add_argument('key_local', type=str, nargs='?', help='Chave local do dispositivo Tuya (para o modo local)')

    # Parsear os argumentos
    args = parser.parse_args()

    if args.mode == 'cloud':
        # Chamar a função para consulta à nuvem
        get_device_status_cloud(args.device_id, args.device_type)
    elif args.mode == 'local':
        if args.ipv5 and args.key_local:
            # Chamar a função para consulta local com base no tipo de dispositivo
            get_device_status_local(args.device_id, args.ipv5, args.key_local, args.device_type)
        else:
            print("Para o modo local, forneça os parâmetros ipv5 e key_local.")
