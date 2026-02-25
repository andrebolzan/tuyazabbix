# tuyazabbix

Scripts Python para integrar dispositivos Tuya com Zabbix, com consulta via cloud e via rede local.

## Dependencias

Instale com:

```bash
pip install -r requirements.txt
```

Dependencias usadas:
- `tinytuya`
- `tabulate`

## Arquivos principais

- `cloudListAllDevices.py`: lista dispositivos da conta Tuya e pode gerar `localKey.txt`.
- `cloudpi.py`: consulta status de dispositivos (cloud ou local) no formato esperado para coleta.

## Configuracao da cloud com .env

O `cloudpi.py` le credenciais do arquivo `.env` no mesmo diretorio do script.

1. Crie o `.env` com base no exemplo:

```bash
cp .env.example .env
```

2. Edite o arquivo `.env`:

```env
TUYA_API_REGION=us
TUYA_API_KEY=sua_api_key
TUYA_API_SECRET=sua_api_secret
```

## Como listar dispositivos da conta

```bash
python3 cloudListAllDevices.py SUA_API_KEY SUA_API_SECRET
```

Para gerar `localKey.txt` automaticamente:

```bash
python3 cloudListAllDevices.py SUA_API_KEY SUA_API_SECRET --geralocalkey
```

## Formato do localKey.txt

Arquivo usado no modo local do `cloudpi.py`.

Cada linha deve ter:

```txt
ID_DO_DISPOSITIVO|LOCAL_KEY
```

Exemplo:

```txt
ebxxxxxxxxxxxxxx|a1b2c3d4e5f6g7h8
```

## Uso do cloudpi.py

Consulta cloud (sensor de temperatura/umidade):

```bash
python3 cloudpi.py cloud sensor ID_DO_DISPOSITIVO
```

Consulta cloud (sensor de fumaca):

```bash
python3 cloudpi.py cloud smoke ID_DO_DISPOSITIVO
```

Consulta local (medidor de energia):

```bash
python3 cloudpi.py local power ID_DO_DISPOSITIVO IP_DO_DISPOSITIVO
```

Observacao:
- No modo local, o script busca a `LOCAL_KEY` no arquivo `localKey.txt`.
- A consulta local costuma ser mais rapida e independe da internet.
