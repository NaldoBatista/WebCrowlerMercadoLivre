from selenium import webdriver
import json

def create_driver():
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.get('https://www.mercadolivre.com.br/ofertas')
    driver.maximize_window()
    return driver

def gerar_json(lista_produtos: any):
    json_lista_produtos = json.dumps(lista_produtos)
    with open('src/produtos_dados.json', 'w') as arq:
        arq.write(json_lista_produtos)


