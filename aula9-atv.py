"""
    Descobrir a qunatidade de paginas disponiveis - ok
    Percorrer todas as paginas - ok 
    Pegar o nome do produto - ok
    Pegar o preço do produto - ok
    Pegar o fabricante - ok
    Pegar o % de desconto do produto - ok
    Salvar em um arquivo xlsx
"""
from bs4 import BeautifulSoup
import requests
import openpyxl

def consultarQuantidadePagina(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        pagina = soup.find('div', class_='page-template') #retorna o primeiro resultado
        div = pagina.find_all('div', class_='text-center pt-3') #retorna tudo dessa class
        div = div[-1].text
        qntd = div.split(" ")[-1]
        return qntd

def ConsultarProdutosPagina(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        pagina = soup.find('div', class_='list-products page-content')
        produtos = pagina.find_all('div', class_='desc position-relative')
        lista_produtos = []

        for item in produtos:
            nome = item.find('h2', class_='title').text.strip()
            fabr = item.find('span', class_='font-size-11 text-primary font-weight-bold').text.strip()
           
            if bool(item.find('p', class_='sale-price')):
                prec = item.find('p', class_='sale-price').text.strip()
            else:
                prec = "Sem estoque"

            if bool(item.find('span', class_='discount')):
                desc = item.find('span', class_='discount').text.strip()
            else:
                desc = ""


            #print(nome, " | ", fabr, " | ", prec, " | ", desc)
            lista_produtos.append([
                fabr,
                nome,
                prec,
                desc 
            ])
        return lista_produtos

def GravarArquivoXLSX(dados, nome_arquivo):
    try:
        excel = openpyxl.Workbook()
        planilha = excel.active

        for linha in dados:
            planilha.append(linha)
        excel.save(nome_arquivo + '.xlsx')
        print('Dados salvos com sucesso, {}.xlsx'.format(nome_arquivo))

    except Exception as ex:
        print('Erro {}'.format(ex))

area = 'hortifruti'

url = 'https://www.superpaguemenos.com.br/{}/'.format(area)
qntd = consultarQuantidadePagina(url)
print(qntd, "quantidade das paginas")

produtos = []
for i in range(1, int(qntd) + 1):
    new_url = url + '?p=' + str(i)
    print(new_url)
    produtos = produtos + ConsultarProdutosPagina(new_url)

GravarArquivoXLSX(produtos, area)