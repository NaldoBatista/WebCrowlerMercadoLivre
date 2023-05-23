from actions_bot.actions_bot import ActionsBot
from selenium.webdriver.common.by import By

class ProdutoPageLocators(object):
    link_inserir_cep = (By.XPATH, '/html/body/header/div/div[4]/div/a')
    input_inserir_cep = (By.XPATH, '//*[@id="addressesForm"]/div/div/div/div[1]/label/div/input')


class ProdutoPage(ActionsBot):
    def __init__(self, driver) -> None:
        super().__init__(driver)

    def inserir_cep(self):
        self.click(ProdutoPageLocators.link_inserir_cep)
        self.write(ProdutoPageLocators.input_inserir_cep, '49100000')

    def calcular_prazo_frete(self):
        pass
