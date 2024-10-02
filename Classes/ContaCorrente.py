# Classe Conta Corrente: Crie uma classe para implementar uma conta corrente. 
# A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
# Os métodos são os seguintes: 
# alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero 
# e os demais atributos são obrigatórios.

class ContaCorrente():
    def __init__ (self,numeroConta,nomeCorrentista,saldo=0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def __str__(self):
        return f'nome: {self.nomeCorrentista} | numero da conta: {self.numeroConta} | saldo: {self.saldo}'
    
    def mudarNome(self,nomeAlterado):
        self.nomeCorrentista = nomeAlterado
        return f'nome alterado para: {self.nomeCorrentista}'
    
    def deposito(self,valorDeposito):
        self.saldo += valorDeposito
        return f'Deposito de {valorDeposito} realizado, saldo alterado para: {self.saldo}'

    def saque(self,valorSaque):
        if self.saldo >= valorSaque:
            self.saldo -= valorSaque 
            return f'Saque de {valorSaque} realizado, saldo alterado para: {self.saldo}'
        else: 
            return 'Saldo insuficiente para saque'