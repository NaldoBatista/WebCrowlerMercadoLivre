from actions_bot.actions_bot import ActionsBot
from selenium.webdriver.common.by import By
from time import sleep

class ProdutoPageLocators(object):
    prazo_frete = [(By.XPATH, '//*[@id="pick_up_summary"]/div/div/p/span[1]'),
                    (By.XPATH, '//*[@id="buybox-form"]/div[2]/div/p/span[1]'),
                    (By.XPATH, '//*[@id="shipping_summary"]/div/div/p/span'),
                    (By.XPATH, '//*[@id="buybox-form"]/div[1]/div/div[1]/p/span[1]')]
                    
class ProdutoPage(ActionsBot):
    def __init__(self, driver) -> None:
        super().__init__(driver)   

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

        

