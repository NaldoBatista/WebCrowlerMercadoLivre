
import json
from flow.raspar_dados import RasparDados
from pages.ofertas_page import OfertasPage
from utils.utils import create_driver


lista_dados_produtos = []
driver = create_driver()

raspar_dados = RasparDados(driver)
ofertas_page = OfertasPage(driver)

for pagina in range(1, 3):
    for produto in range(1, 5):
        dados_produto = raspar_dados.raspar_dados_produto(produto, pagina)
        lista_dados_produtos.append(dados_produto)
    ofertas_page.proxima_pagina()
    

#print(lista_dados_produtos)
json_lista_dados_produtos = json.dumps(lista_dados_produtos)
with open('produtos_dados.json', 'w') as arq:
    arq.write(json_lista_dados_produtos)