from actions_bot.actions_bot import ActionsBot
from selenium.webdriver.common.by import By
from time import sleep

class Locators(object):  
    link_inserir_cep = (By.XPATH, '/html/body/header/div/div[4]/div/a')
    iframe_cep = [(By.XPATH, '/html/body/div[3]/div[1]/iframe'),
                  (By.XPATH, '/html/body/div[4]/div[1]/iframe')]
    input_inserir_cep = (By.XPATH, '//*[@id="addressesForm"]/div/div/div/div[1]/label/div/input')
    btn_usar = (By.XPATH, '//*[@id="addressesForm"]/div/div/div/div[1]/label/div/div/button')


class OfertasPage(ActionsBot):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def inserir_cep(self):
        for xpath in Locators.iframe_cep:
            try:
                self.click(Locators.link_inserir_cep)
                sleep(5)
                iframe_cep = self.driver.find_element(*xpath)
                self.driver.switch_to.frame(iframe_cep)
                self.write(Locators.input_inserir_cep, '49100000')
                self.click(Locators.btn_usar)
                self.driver.switch_to.default_content()
                print('Cep inserido com sucesso!')
                break
            except:
                print('Falha ao inserir cep!')
                self.driver.refresh()

    def mover_para_elemento(self, index_prod: int, num_page: int):
        try:
            self.move_to_element(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]'))
        except Exception as e:
            print(e)
            print(f'Falha ao mover para o elemento {index_prod} (página{num_page})')

    
    def get_nome_produto(self, index_prod: int, num_page: int):
        try:
            return self.get_text(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[2]/p')
            )
        except Exception as e:
            print(f'Falha ao pegar o nome do produto {index_prod} (página {num_page})')
    
    def get_valor_atual(self, index_prod: int, num_page: int):
        try:
            return self.get_text(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[2]/div[2]/div/span[1]/span[3]')
            )
        except Exception as e:
          #print(e)
          print(f'Falha ao pegar o valor atual do produto {index_prod} (página {num_page})')  
    
    def get_valor_antigo(self, index_prod: int, num_page: int):
        try:
            return self.get_text(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[2]/div[2]/s/span[3]')
            )
        except Exception as e:
            #print(e)
            print(f'Falha ao pegar o valor antigo do produto {index_prod} (página {num_page})')
    
    def get_desconto(self, index_prod: int, num_page: int):
        try:
            return self.get_text(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[2]/div[2]/div/span[2]')
            ).replace(' OFF', '')
        except:
            print(f'Falha ao pegar o desconto do produto {index_prod} (página {num_page})')
    
    def get_link_imagem(self, index_prod: int, num_page: int):
        try:
            return self.get_link_img(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[1]/img')
            )
        except:
            print(f'Falha ao pegar o link da imagem do produto {index_prod} (página {num_page})')
    
    def get_nome_loja(self, index_prod: int, num_page: int):
        try:
            return self.get_text(
                (By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]/div/a/div/div[2]/span[2]')
            ).replace('por ', '')
        except:
            print(f'Falha ao pegar o nome da loja do produto {index_prod} (página {num_page})')

    def proxima_pagina(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            self.click(
            (By.XPATH, '//*[@id="root-app"]/div[2]/div[2]/div/nav/ul/li[13]/a/span[1]')
        )
        except:
            print('Falha ao ir para proxima página!')

    def go_pagina_produto(self, index_prod: int, num_page: int):
        self.click((By.XPATH, f'//*[@id="root-app"]/div[2]/div[2]/div/ol/li[{index_prod}]'))

