class recibo:
    def __init__(self, nome):
        self._nome = nome
        self._valor = 0
        self._descricao = 'Sistema genérico de qualidade'
        #self._nome = nome ------> publico
        #self.nome = nome -------> privado

    def __str__(self):
        texto = 'Recebemos de {} a quantia de R${:.2f}'.format(self._nome, self._valor)
        descricao = 'Referente {}'.format(self._descricao)
        dados = '{}\n {}'.format(descricao, texto)
        return dados
    

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, value):
        self._valor = value

    def descricao(self,value):
        self._descricao = value