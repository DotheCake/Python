'''
Atividade: juntar as informações de duas planilhas(categorias e produtos)
    - abrir o primeiro arquivo CSV ✔
    - guardar a info do 1º arquivo CSV ✔
    - abrir o segundo arquivo CSV ✔
    - guardar as infos do 2º arquivo CSV ✔
    - mesclar / tratar as infos com os valores correspondentes
    - manter somente as infos necessarias
    - converter as infos para o xlsx
'''
import openpyxl


def carregarCSV(nome_arquivo):
    dados_arquivo = open (nome_arquivo + '.csv', 'r', encoding = 'utf-8')

    lista_info = []
    for linha in dados_arquivo:
        colunas = (linha.strip().split(';'))
        lista_info.append(colunas)
    return lista_info

def concatenarArquivosCSV(categoriasCSV, produtosCSV):
    dados_csv=[]
    dados_csv.append([
        'id',
        'nome_produto',
        'quantidade',
        'valor_venda',
        'valor_compra',
        'id_categoria',
        'nome_categoria'

    ])
    for produto in produtosCSV:
        index = int(produto[2]) - 1
        #dados_csv.append([produto, *categoriasCSV[index]])
        dados_csv.append([
            produto[0],
            produto[1],
            produto[4],
            produto[8],
            produto[9],
            categoriasCSV[index][0],
            categoriasCSV[index][1]
        ])

    return dados_csv

def gravarArquivoXLSX(dados, nome_arquivo):
    try:
        excel = openpyxl.Workbook() # cria o excel
        planilha = excel.active # pega a primeira planilha ativa

        for linha in dados:
            planilha.append(linha)
        excel.save(nome_arquivo + '.xlsx')
        print('Dados salvos com sucesso no arquivo {}.xlsx'.format(nome_arquivo))
    except Exception as ex:
        print('Ocorreu um erro: {}'.format(ex))

dados_categoria = carregarCSV('categorias')
dados_produto = carregarCSV('produtos')
dados_concatenados = concatenarArquivosCSV(dados_categoria, dados_produto)

gravarArquivoXLSX(dados_concatenados, 'infos tratadas')
