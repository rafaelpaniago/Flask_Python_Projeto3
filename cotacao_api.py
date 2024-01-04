import requests
import json

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
cotacoes = cotacoes.json()
print(cotacoes)

# Agora vamos buscar a cotação do dolar
cotacao_dolar = float(cotacoes['USDBRL']['bid'])
cotacao_euro = float(cotacoes['EURBRL']['bid'])
cotacao_bitcoin = float(cotacoes['BTCBRL']['bid'])
vDigitado = float(input("Digite um valor: "))
print("Em DÓLARES é: ", (vDigitado / cotacao_dolar), "\nEm EUROS: ", (vDigitado / cotacao_euro), "\nEm BITCOINS: ", (vDigitado / cotacao_bitcoin))
