caminho_arquivo = 'categorias.csv'

# r --> read
# w --> write

categorias = open(caminho_arquivo, 'r', encoding='utf-8')

lista_categorias = {}

for linha in categorias:
    colunas = linha.strip().split(';')
    lista_categorias[colunas[0]] = [colunas[1], colunas[2]]

    print(lista_categorias)