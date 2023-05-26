from actions_bot.actions_bot import ActionsBot
from selenium.webdriver.common.by import By
from time import sleep

class ProdutoPageLocators(object):
    link_inserir_cep = (By.XPATH, '/html/body/header/div/div[4]/div/a')
    iframe_cep = (By.XPATH, '/html/body/div[4]/div[1]/iframe')
    input_inserir_cep = (By.XPATH, '//*[@id="addressesForm"]/div/div/div/div[1]/label/div/input')
    btn_usar = (By.XPATH, '//*[@id="addressesForm"]/div/div/div/div[1]/label/div/div/button')

    prazo_frete = [(By.XPATH, '//*[@id="pick_up_summary"]/div/div/p/span[1]'),
                    (By.XPATH, '//*[@id="buybox-form"]/div[2]/div/p/span[1]'),
                    (By.XPATH, '//*[@id="shipping_summary"]/div/div/p/span'),
                    (By.XPATH, '//*[@id="buybox-form"]/div[1]/div/div[1]/p/span[1]')]
                    
class ProdutoPage(ActionsBot):
    def __init__(self, driver) -> None:
        super().__init__(driver)   

    def inserir_cep(self):
        handles = self.driver.window_handles
        self.click(ProdutoPageLocators.link_inserir_cep)
        sleep(5)
        iframe_cep = self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/iframe')
        self.driver.switch_to.frame(iframe_cep)
        self.write(ProdutoPageLocators.input_inserir_cep, '49100000')
        self.click(ProdutoPageLocators.btn_usar)
        self.driver.switch_to.default_content()
        print('sucesso!!!')
        sleep(2)

    def calcular_prazo_frete(self):
        for i in range(0, 5):
            try:
                prazo = self.get_text(ProdutoPageLocators.prazo_frete[i])
                print(prazo)
                break
            except:
                print(f'Calcular frete erro tentativa { i+1 }')
        return prazo
    
    def go_ofertas_page(self):
        self.driver.back()

        

