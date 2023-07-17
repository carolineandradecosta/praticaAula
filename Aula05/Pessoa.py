# Manipulação de leitura de JSON no Python

import json

json_data = '{"nome": "Amanda", "idade": 28, "cidade": "Joao Pessoa"}'
data = json.loads(json_data)

print(data["nome"])
print(data["idade"])
print(data["cidade"])
