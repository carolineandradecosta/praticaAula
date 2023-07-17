# Manipulação de leitura de JSON no Python

import json

json_data = '{"nome": "Caroline", "idade": 31, "cidade": "Campina Grande"}'
data = json.loads(json_data)

print(data["nome"])
print(data["idade"])
print(data["cidade"])
