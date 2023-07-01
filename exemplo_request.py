import requests

url = 'https://api.adviceslip.com/advice'

    #mostra 10 frases da api
for i in range(10):
    resposta = requests.get(url)
    resposta = resposta.json()
    # print(resposta.json())

    print(resposta['slip']['advice'])



