import openpyxl

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

arquivo_excel = 'minhas_series.xlsx'

dados = [
    ['The Big Bang Theory', '2007'],
    ['One piece', '1991']
]

criar_planilha(arquivo_excel, dados)