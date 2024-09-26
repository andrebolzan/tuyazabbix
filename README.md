# tuyazabbix
scrip em python para integracao da API tuya com Zabbix


Os script são baseador na classe tinytuya disponivel no git:

https://github.com/jasonacox/tinytuya

Necessario fazer a instalação
pip install tinytuya

Usamos tambe classe de tabulação para gerar a lista:
pip install tabulate

o scrip cloudListAllDevices.py lista todos os disponsitovos e seus dados 

Precisamos de 3 informações importantes 
1) ID dispositivos, usado para consultas em nuvem e local
3) MAC address , usado para fixar IP nos IOTs que serão consultados locamente.
4) Modelo do dispositivos para podere classificar qual tipo de consulta fazer pois existe alguns "sub modelos, Senosr temperatura com indicador de bateria, sem indiciador, etc

 X ) KeyLocal, chave local que sera usada para consultas locais diretamente em dispositivos |


Para rodar basta rodar scrup pasando userKey  e "senha"
CludListAll.py UserKEYtvhy785s559hr SecreTEaaXX:xx:xx:xx:xx::xxdb3ISSOVALEOURO

Gerando lista
nome | ID | Chave Local | MAC | modelo 

Caso possivel recomendo usar consultas locais, elas são mais atualizadas , mais rapidas, não depdentes de nada alems do equipamento e não custa dinheiro.

Para rodar basta rodar scrup pasando userKey , "senha" , passando parametro --gerLocalKey
CludListAll.py UserKEYtvhy785s559hr SecreTEaaXX:xx:xx:xx:xx::xxdb3ISSOVALEOURO --gerLocalKey

sera gerado arquivo locakKey.txt contendo ID e localKey , como as locakey usar muitos carecteres especiais fica "impossivel" usar ela diretamente no zabbix, para usar diretamente no zabbix você tem que tratar a string.


O Scipt cloudpi.py faz sonultas diretamente na nuvem da Tuya ou diretamente no disponsitovso.

para realiza as consulta você precisa cadastra dentro do scrip sua key e sua chave da API tuya (logo logo vou fazer um passo a passo em video)

Consutas em nuvem temperatura # esse numero nucna numa, mesmo se mudar de conta o ID segue dispostivos.
python3 cloudpi.py cloud sensor ID_DISPOSTIVOS_eba4736c777gkly 


Consutas em nuvem temperatura # esse numero nucna numa, mesmo se mudar de conta o ID segue dispostivos.
python3 cloudpi.py cloud smoke ID_DISPOSTIVOS_e24736c777gkly


Consutla locamente dos Wattimetros (power metter) 
Muito "chato" fazer essac consutlas, pois qualquer caracter errado ele não retorna os valores.
Vantagem que tempo de coleta é muito rapido e pode ser feito sem internet.
EX: python3 cloudpi.py local power ID_DISPOSTIVOS IPv4_dispositovos 'LOCALKEY_pegarcomOtroScirp'

python3 cloudpi.py local power ID_DISPOSTIVOS_e0c8aef4c7us 192.168.0.169


Sempre retora 2 valores de controle:
1º se dispostivos Online ultimo Codigo de erro


Consutla me nuvem:
sensor de temperatrua modelos:
TH01CB3Sxxxxxxxxxxx
温湿度传感器wifi

Sensor de fumaça modelos:
烟雾报警器              | YG400A-CBU

Consukta loca
Watimmetros/ medidos de consumo/tensao: 
WiFi Digital Meter | PJ-1103 

