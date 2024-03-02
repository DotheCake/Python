import openpyxl

'''
atividade: converter o arquivo csv em xlsx
- identificar o nome do arquivo - ✔
- abrir o arquivo - ✔
- guardar as informações no arquivo - ✔
- criar um novo arquivo xls
- iserir as informações guardadas no novo arquivo
'''

def carregarCSV(nome_arquivo):
    dados_arquivo = open (nome_arquivo + '.csv', 'r', encoding = 'utf-8')

    lista_info = []
    for linha in dados_arquivo:
        colunas = (linha.strip().split(';'))
        lista_info.append(colunas)
    return lista_info

def criarXLSX(dados, nome_arquivo):
    try:
        excel = openpyxl.Workbook()#cria o excel
        planilha = excel.active # pega a primeira planilha disponivel

        for linha in dados:
            planilha.append(linha)
        excel.save(nome_arquivo +'.xlsx')
        print('Dados salvos com sucesso no arquivo {}.xlxs'.fomrat(nome_arquivo))
    except Exception as ex:
        print('Ocorreu um erro {}'.format(ex))

# nome-arquivo = input('Informe o nome do arquivo: ')
nome_arquivo = 'categorias'
dados_csv = carregarCSV(nome_arquivo)
carregarCSV(dados_csv,nome_arquivo)