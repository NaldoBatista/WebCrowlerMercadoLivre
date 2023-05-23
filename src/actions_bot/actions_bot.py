from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ActionsBot(object):
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_text(self, locator):
       element = self.wait.until(EC.visibility_of_element_located(locator))
       return element.text

    def get_link_img(self, locator):
        element = self.driver.find_element(*locator)
        return element.get_attribute('src')
    
    def move_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def write(self, locator, text: str):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear().send_keys(text)