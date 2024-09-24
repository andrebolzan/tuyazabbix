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
+------------------+--------------------+------------------+-------------------------+-------------+------------------+----------+
| name             | id                 | key              | mac                     | category    | product_name     | model    |
+==================+====================+==================+=========================+=============+=================+============+
| Ar Bibi          | ebc53bxxxxxxxfzpyp | xxxxxxxxxxxxxxxx |  XX:xx:xx:xx:xx::xx     | infrared_ac | 空调             |           |
+------------------+-----------------------+------------------+-------------------------+-------------+-------------------------------------+----------------------------+
| GWZig            | eb7ffxxxxxxx9alecs | xxxxxxxxxxxxxxxx | XX:xx:xx:xx:xx::xx       | wg2         | NH-HG小网关     | ZHUB-W    |
+------------------+--------------------+------------------+-------------------------+-------------+-------------------------------------+----------------------------+
| P02-F.Vermelha   | exxxxxxxxxxx4c4wg1 | wxxxxxxxxxxxxxxF | XX:xx:xx:xx:xx::xx       | aqcz        | WiFi Digital Meter  | PJ-1103                    |
+------------------+--------------------+------------------+-------------------------+-------------+-------------------------------------+----------------------------+
| porta 01         | eb32dexxxxxxx9     | 40xxxxxxxxxxxx05 | XX:xx:xx:xx:xx::xx       | jtmspro     | 蓝牙锁               | C501                       |
+------------------+--------------------+------------------+-------------------------+-------------+-------------------------------------+----------------------------+
| porta 01         | eb9exxxxxxxxxxccmz | bxxxxxxxxxxxxxxd |XX:xx:xx:xx:xx::xx       | jtmspro     | WIFI智能门锁          | B509                       |
+------------------+--------------------+------------------+-------------------------+-------------+-------------------------------------+----------------------------+
| quadro 01       | ebxxxxxxxxxxxxxXlvf | Sxxxxxxxxxxxxxx{ | XX:xx:xx:xx:xx::xx:52:62 | zndb        | Zigbee Dual Meter    | PJ1203A                    |
+------------------+--------------------+------------------+-------------------------+-------------+-------------------------------------+----------------------------+
| quarto 02       | ebxxxxxxxxxxxxxxxuf | 7cxxxxxxxxxxxxx4 | XX:xx:xx:xx:xx::xx       | kg          | Wifi smart 1CH switch| KG31WF+RF KG27WF           |
+------------------+--------------------+------------------+-------------------------+-------------+-------------------------------------+----------------------------+


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


