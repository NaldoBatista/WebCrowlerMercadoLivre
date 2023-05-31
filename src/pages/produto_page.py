from actions_bot.actions_bot import ActionsBot
from selenium.webdriver.common.by import By

class Locators(object):
    # O xpath do campo prazo muda de acordo com o produto.
    # Sendo assim, mapiei os possíveis xpath.
    prazo_frete = [(By.XPATH, '//*[@id="pick_up_summary"]/div/div/p/span[1]'),
                    (By.XPATH, '//*[@id="buybox-form"]/div[2]/div/p/span[1]'),
                    (By.XPATH, '//*[@id="shipping_summary"]/div/div/p/span'),
                    (By.XPATH, '//*[@id="buybox-form"]/div[1]/div/div[1]/p/span[1]')]
                    
class ProdutoPage(ActionsBot):
    def __init__(self, driver) -> None:
        super().__init__(driver)   

    def calcular_prazo_frete(self, index_prod, num_page):
        prazo = None
        for xpath in Locators.prazo_frete:
            try:
                prazo = self.get_text(xpath)
                break
            except:
                print(f'Falha ao calcular frete do produto {index_prod} (página {num_page})')
        return prazo
    
    def go_ofertas_page(self):
        self.driver.back()

        

