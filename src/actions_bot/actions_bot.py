from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ActionsBot(object):
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 1)

    def click(self, locator):
        elemento = self.wait.until(EC.element_to_be_clickable(locator))
        elemento.click()

    def get_text(self, locator):
       elemento = self.wait.until(EC.visibility_of_element_located(locator))
       return elemento.text

    def get_link_img(self, locator):
        elemento = self.driver.find_element(*locator)
        return elemento.get_attribute('src')
    
    def move_to_element(self, locator):
        elemento = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento)