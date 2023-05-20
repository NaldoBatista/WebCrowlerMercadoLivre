from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from actions_bot.actions_bot import ActionsBot
from pages.ofertas_page import OfertasPage

produto_atributos = {
    "nome_do_produto": "",
    "valor_atual": "",
    "valor_antigo": "",
    "desconto": "",
    "link_da_imagem": "",
    "prazo_do_frete": "",
    "nome_da_loja_vendedora": ''
}

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.mercadolivre.com.br/ofertas')
driver.maximize_window()
index = 1

ofertas_page = OfertasPage(driver)
'''
produto_atributos["nome_do_produto"] = ofertas_page.get_nome_produto(index)
produto_atributos["valor_atual"] = ofertas_page.get_valor_atual(index)
produto_atributos["valor_antigo"] = ofertas_page.get_valor_antigo(index)
produto_atributos["desconto"] = ofertas_page.get_desconto(index)
produto_atributos["link_da_imagem"] = ofertas_page.get_link_imagem(index)
produto_atributos["nome_da_loja_vendedora"] = ofertas_page.get_nome_loja(index)
'''
ofertas_page.proxima_pagina()
sleep(1)
ofertas_page.proxima_pagina()
sleep(1)

'''
print("\n==================================")
print(produto_atributos)
print("==================================\n")
'''


