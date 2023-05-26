from pages.ofertas_page import OfertasPage
from pages.produto_page import ProdutoPage

class RasparDados(object):
    def __init__(self, driver) -> None:
        self.driver = driver
    
    def raspar_dados_produto(self, index_prod: int, num_page: int):
        produto_atributos = {}
        produto_page = ProdutoPage(self.driver)
        ofertas_page = OfertasPage(self.driver)
        ofertas_page.mover_para_elemento(index_prod, num_page)
        ofertas_page.go_pagina_produto(index_prod, num_page)
        produto_atributos["prazo_frete"] = produto_page.calcular_prazo_frete()
        produto_page.go_ofertas_page()
        produto_atributos["nome_do_produto"] = ofertas_page.get_nome_produto(index_prod, num_page)
        produto_atributos["valor_atual"] = ofertas_page.get_valor_atual(index_prod, num_page)
        produto_atributos["valor_antigo"] = ofertas_page.get_valor_antigo(index_prod, num_page)
        produto_atributos["desconto"] = ofertas_page.get_desconto(index_prod, num_page)
        produto_atributos["link_da_imagem"] = ofertas_page.get_link_imagem(index_prod, num_page)
        produto_atributos["nome_da_loja_vendedora"] = ofertas_page.get_nome_loja(index_prod, num_page)
        return produto_atributos

