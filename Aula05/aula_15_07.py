# Refatoração para fazer em casa (Exercício 01):
# Abastecer o Json do input do usuário.

import json

# Trazendo dados de um json de forma clean
json_data = '{"id": 1, "nome": "Caroline", "saldo": 4000.00}'
# Transformando a JSON em dicionário, o python não é capaz de acessar um json diretamente.
data = json.loads(json_data)

print(data["id"])
print(data["nome"])
print(data["saldo"])
