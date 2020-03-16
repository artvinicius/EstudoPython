import requests
import json

url = 'https://api.marquesconsult.com.br/v2/auth/login'

payload = {'cpf': '11111111111', 'senha': '123456'}
headers = {'content-type': 'application/json'}

r = requests.post(url, data=json.dumps(payload), headers=headers)
resposta = r.json()
token = resposta['token']


headers = {'Authorization': 'Bearer ' + token}
url = 'https://api.marquesconsult.com.br/v2/esus/me/permissoes'
r = requests.get(url, headers=headers)
print(r.text)

headers = {'Authorization': 'Bearer ' + token}
url = 'https://api.marquesconsult.com.br/v2/esus/municipios/DB_30/relatorios/medicos/medico-individual-diario-unidade?comp=2020-01'
r = requests.get(url, headers=headers)
print(r.text)