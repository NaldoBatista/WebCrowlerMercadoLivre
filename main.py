from selenium import webdriver
from flow.raspar_dados import RasparDados
from pages.ofertas_page import OfertasPage

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.mercadolivre.com.br/ofertas')
driver.maximize_window()

lista_dados_produtos = []

raspar_dados = RasparDados(driver)
ofertas_page = OfertasPage(driver)

for pagina in range(2):
    for produto in range(1, 4):
        dados_produto = raspar_dados.raspar_dados_produto(produto)
        lista_dados_produtos.append(dados_produto)
    ofertas_page.proxima_pagina()
    

print(lista_dados_produtos)