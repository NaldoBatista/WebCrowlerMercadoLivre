from selenium import webdriver

def create_driver():
    driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
    driver.get('https://www.mercadolivre.com.br/ofertas')
    driver.maximize_window()
    return driver