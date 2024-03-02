import openpyxl

'''
atividade: converter o arquivo csv em xlsx
- identificar o nome do arquivo
- abrir o arquivo
- guardar as informações no arquivo
- criar um novo arquivo xls
- iserir as informações guardadas no novo arquivo
'''

# nome-arquivo = input('Informe o nome do arquivo: ')
nome_arquivo = 'categorias.csv'

def criar_planilha(arquivo, dados):
    try:
        wb = openpyxl.Workbook()

        planilha = wb.active # vai pegar a primeira aba ativa

        for linha in dados:
            planilha.append(linha) #para adcionar mais informações

        wb.save(arquivo)

        print('Dados salvo com sucesso no arquivo {}'.format(arquivo))

    except Exception as ex:
        print('Ocorreu um erro {}'.format(ex))

arquivo_excel = 'categorias_.xlsx'

dados = [
    ['id', 'Categoria'],
    ['1','Bebidas, Refrigerantes, cafés, chás, cervejas e cervejas'],
    ['2','Condimentos, Molhos doces e salgados, condimentos, patês e temperos'],
    ['3','Confeitaria, Doces, sobremesas, doces e pães doces'],
    ['4','Lácteos, Leites e Queijos'],
    ['5','Grãos / Cereais, Pães, biscoitos, massas e cereais'],
    ['6','Carnes / Aves, Preparadas de carnes'],
    ['7','Processados, Frutas secas e coalhada de feijão'],
    ['8','Frutos do mar, Algas e peixes']
]

criar_planilha(arquivo_excel, dados)