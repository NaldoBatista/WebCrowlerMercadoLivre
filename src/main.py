from flow.raspar_dados import RasparDados
from pages.ofertas_page import OfertasPage
from utils.utils import create_driver, gerar_json
from time import sleep

def web_crowler_mercado_livre_ofertas(num_pages: int):
    driver = create_driver()
    ofertas_page = OfertasPage(driver)
    sleep(3)
    ofertas_page.inserir_cep()
    raspar_dados = RasparDados(driver)
    lista_dados_produtos = []
    sleep(5)

    # Esse laço percorre as páginas de oferta previamente definidas
    for pagina in range(1, num_pages + 1):
        # Esse laço percorre todos os 48 produtos de cada página
        for produto in range(1, 49):
            dados_produto = raspar_dados.raspar_dados_produto(produto, pagina)
            lista_dados_produtos.append(dados_produto)
        ofertas_page.proxima_pagina()
    return lista_dados_produtos

if __name__ == '__main__':
    numero_de_paginas = 1
    lista_dados_produtos = []

    lista_dados_produtos =  web_crowler_mercado_livre_ofertas(numero_de_paginas)
    gerar_json(lista_dados_produtos)