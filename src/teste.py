from utils.utils import create_driver
from pages.ofertas_page import OfertasPage
from pages.produto_page import ProdutoPage
from time import sleep


driver = create_driver()
ofertas_page = OfertasPage(driver)
produto_page = ProdutoPage(driver)
ofertas_page.go_pagina_produto(1, 1)
produto_page.inserir_cep()


sleep(4)

