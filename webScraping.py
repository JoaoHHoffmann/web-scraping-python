import requests
from bs4 import BeautifulSoup

# Requisição HTTP para obter o conteúdo da página
pagina = requests.get("https://quotes.toscrape.com/")

dados_pagina = BeautifulSoup(pagina.text, 'html.parser')

print(dados_pagina.prettify())