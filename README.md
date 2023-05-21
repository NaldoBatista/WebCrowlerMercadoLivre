# WebCrowlerMercadoLivre

## Primeira Parte

Essa solucao consiste em um RPA (Robotic Process Automatic) para raspar dados da página de ofertas do mercado livre.
Para o desenvolvimeto dessa solução foi utilizada a linguagem de programação python e o framework selenium.

### Requiriments
Para a execução desse script é precisso as seguintes tecnologias:  
Python 3.11.3  
Selenium 4.9.1

### Funcionamento 
A ideia principal desse projeto é percorrer todos os produtos da página de ofertas coletando todos os atributos do produto em quantas páginas o usuário desejar. 
Durante a execução do script, será exibido um log no terminal informando qual coleta de atributo ocorreu falha. 
Ao final da execução será fornecido um arquivo .json contendo uma lista de produtos com seus respectivos atributos.

## Segunda Parte
 
### Susgestão de Solução Para o Problema de Escalonamento Que Foi Apresentado No Desafio

1 - Dividir o problema em partes menores. Dividir em taresfas de 500 linha, por exemplo.  
2 - Exetutar o RPA em paralelo. Usando programação multithreading ou executando em várias maquinas.  
3 - Acompanhar e monitorar a execução para evitar repetição de trabalho e inconsistencias na geração dos dados.  
4 - Validar os dados de acordo com o que é esperado.

Dessa forma é possível reduzir significativamente o tempo de processamento da coleta do dados. Para isso, é precisso considerar os limites técnicos da infraestrutura do ambiente de produção. Pois, a eficiência na coleta dos dados é um fator relevante nesse tipo de aplicação.



