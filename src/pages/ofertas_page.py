from actions_bot.actions_bot import ActionsBot
from selenium.webdriver.common.by import By

class OfertasPage(ActionsBot):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def mover_para_elemento(self, index_prod: int, numPage: int):
        try:
            self.move_to_element(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]'))
        except Exception as e:
            print(e)
            print(f'Falha ao mover para o elemento {index_prod} (página{numPage})')

    
    def get_nome_produto(self, index_prod: int, numPage: int):
        try:
            return self.get_text(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[2]/p')
            )
        except Exception as e:
            print(f'Falha ao pegar o nome do produto {index_prod} (página {numPage})')
    
    def get_valor_atual(self, index_prod: int, numPage: int):
        try:
            return self.get_text(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[2]/div[2]/div/span[1]/span[3]')
            )
        except Exception as e:
          #print(e)
          print(f'Falha ao pegar o valor atual do produto {index_prod} (página {numPage})')  
    
    def get_valor_antigo(self, index_prod: int, numPage: int):
        try:
            return self.get_text(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[2]/div[2]/s/span[3]')
            )
        except Exception as e:
            #print(e)
            print(f'Falha ao pegar o valor antigo do produto {index_prod} (página {numPage})')
    
    def get_desconto(self, index_prod: int, numPage: int):
        try:
            return self.get_text(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[2]/div[2]/div/span[2]')
            ).replace(' OFF', '')
        except:
            print(f'Falha ao pegar o desconto do produto {index_prod} (página {numPage})')
    
    def get_link_imagem(self, index_prod: int, numPage: int):
        try:
            return self.get_link_img(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[1]/img')
            )
        except:
            print(f'Falha ao pegar o link da imagem do produto {index_prod} (página {numPage})')
    
    def get_nome_loja(self, index_prod: int, numPage: int):
        try:
            return self.get_text(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[2]/span[2]')
            ).replace('por ', '')
        except:
            print(f'Falha ao pegar o nome da loja do produto {index_prod} (página {numPage})')

    def proxima_pagina(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.click(
            (By.XPATH, '//*[@id="root-app"]/div[2]/div[2]/div/nav/ul/li[13]/a/span[1]')
        )
        except:
            print('Falha ao ir para proxima página!')

