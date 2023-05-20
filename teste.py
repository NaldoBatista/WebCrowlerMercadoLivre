from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
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

sleep(3)

indice_produto = 1
#link_card_produto = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]')
#link_card_produto.click()

link_nome_produto = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[2]/p')
link_valor_atual = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[2]/div[2]/div/span[1]/span[3]')
link_valor_antigo = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[2]/div[2]/s/span[3]')
link_desconto = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[2]/div[2]/div/span[2]')
link_imagem = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[1]/img')
link_loja_vendedora = driver.find_element(By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{indice_produto}]/div/a/div/div[2]/span[2]')

#campo_valor_antigo = driver.find_element(By.XPATH, f'')


produto_atributos['nome_do_produto'] = link_nome_produto.text
produto_atributos['valor_atual'] = link_valor_atual.text
produto_atributos['valor_antigo'] = link_valor_antigo.text
produto_atributos['desconto'] = link_desconto.text.replace(' OFF', '')
produto_atributos['link_da_imagem'] = link_imagem.get_attribute('src')
produto_atributos['nome_da_loja_vendedora'] = link_loja_vendedora.text.replace('por ', '')

print("\n=======================================")
print(produto_atributos)
print("=======================================\n")
sleep(5)