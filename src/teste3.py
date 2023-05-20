from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from actions_bot.actions_bot import ActionsBot
from time import sleep

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
action_bot = ActionsBot(driver)

indice_produto = 1

link_nome_produto = (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[2]/p')
link_valor_atual = (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[2]/div[2]/div/span[1]/span[3]')
link_valor_antigo = (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[2]/div[2]/s/span[3]')
link_desconto = (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[2]/div[2]/div/span[2]')
link_imagem = (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[1]/img')
link_loja_vendedora = (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[2]/span[2]')


produto_atributos['nome_do_produto'] = action_bot.get_text(link_nome_produto)
produto_atributos['valor_atual'] = action_bot.get_text(link_valor_atual)
produto_atributos['valor_antigo'] = action_bot.get_text(link_valor_antigo)
produto_atributos['desconto'] = action_bot.get_text(link_desconto).replace(' OFF', '')
produto_atributos['link_da_imagem'] = driver.find_element(*link_imagem).get_attribute('src')
produto_atributos['nome_da_loja_vendedora'] = action_bot.get_text(link_loja_vendedora).replace('por ', '')

print("\n=======================================")
print(produto_atributos)
print("=======================================\n")
sleep(5)