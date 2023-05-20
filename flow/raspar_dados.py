from pages.ofertas_page import OfertasPage

class RasparDados(object):
    def __init__(self, driver) -> None:
        self.driver = driver
    
    def raspar_dados_produto(self, index_prod: int):
        produto_atributos = {}
        ofertas_page = OfertasPage(self.driver)
        produto_atributos["nome_do_produto"] = ofertas_page.get_nome_produto(index_prod)
        produto_atributos["valor_atual"] = ofertas_page.get_valor_atual(index_prod)
        produto_atributos["valor_antigo"] = ofertas_page.get_valor_antigo(index_prod)
        produto_atributos["desconto"] = ofertas_page.get_desconto(index_prod)
        produto_atributos["link_da_imagem"] = ofertas_page.get_link_imagem(index_prod)
        produto_atributos["nome_da_loja_vendedora"] = ofertas_page.get_nome_loja(index_prod)
        return produto_atributos

