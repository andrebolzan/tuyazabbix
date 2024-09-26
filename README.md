# tuyazabbix
scrip em python para integracao da API tuya com Zabbix


Os script são baseador na classe tinytuya disponivel no git:

https://github.com/jasonacox/tinytuya

Necessario fazer a instalação
pip install tinytuya

Usamos tambe classe de tabulação para gerar a lista:
pip install tabulate

o scrip cloudListAllDevices.py lista todos os disponsitovos e suas chaves locay usadas na consulta 

Precisamos de 3 informações importantes 
1) ID dispositivos, usado para consultas em nuvem e local
2) KeyLocal, chave local que sera usada para consultas locais diretamente em dispositivos
3) MAC address , usado para fixar IP nos IOTs que serão consultados locamente.
4) Modelo do dispositivos para ajdua em debugs, pois enventualmente temos modelos que tem pequena variavel e precisa de coletas 

python3 cludListAll.py UserKEYtvhy785s559hr SecreTEaaXX:xx:xx:xx:xx::xxdb3ISSOVALEOURO
+--------+---------+--------+--------+-------------+------------------+----------+
| name   | id      | key    | mac    | category    | product_name     | model    |
+========+=========+========+========+=============+========          +============+
| NOME1  | IDxpto1 | Chave1 |  MA:C1 | Cat1        | NomeP1 |           |
+--------------+---------+--------------+----------+--------+--------------+-----------+
| NOME2  | IDxpto2 | Chave2 | MA:C1  | Cat2        | NomeP2 | ZHUB-W    |
+--------------+---------+-------------+--------------------+-------------+------------------+----------+
| NOME3  | IDxpto3 | Chave3 | MA:C1  | Cat1        | NomeP3 | PJ-1103   |
+-----------+----------+-------------+---------------------+-------------+------------------+--------+


Scip cloudpi.py faz sonultas diretamente na nuvem da Tuya ou diretamente no disponsitovso.

Consutla me nuvem:
sensor de temperatrua modelos:
TH01CB3Sxxxxxxxxxxx
温湿度传感器wifi

Sensor de fumaça modelos:
烟雾报警器              | YG400A-CBU

Consukta loca
Watimmetros/ medidos de consumo/tensao: 
WiFi Digital Meter | PJ-1103 

para realiza as consulta você precisa cadastra dentro do scrip sua key e sua chave da API tuya (logo logo vou fazer um passo a passo em video)

Consutas em nuvem temperatura # esse numero nucna numa, mesmo se mudar de conta o ID segue dispostivos.
python3 cloudpi.py cloud sensor ID_DISPOSTIVOS_eba4736c777gkly 


Consutas em nuvem temperatura # esse numero nucna numa, mesmo se mudar de conta o ID segue dispostivos.
python3 cloudpi.py cloud smoke ID_DISPOSTIVOS_e24736c777gkly


Consutla locamente dos Wattimetros (power metter) 
Muito "chato" fazer essac consutlas, pois qualquer caracter errado ele não retorna os valores.
Vantagem que tempo de coleta é muito rapido e pode ser feito sem internet.
EX: python3 cloudpi.py local power ID_DISPOSTIVOS IPv4_dispositovos 'LOCALKEY_pegarcomOtroScirp'

python3 cloudpi.py local power ID_DISPOSTIVOS_e0c8aef4c7us 192.168.0.169 'iMR>sdsdsdsdsdc'


Sempre retora 2 valores de controle:
1º se dispostivos Online ultimo Codigo de erro


Para os WiFi Digital Meter usando lcoaente precisamos do locakkey


