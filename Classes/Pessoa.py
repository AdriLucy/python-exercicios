# Classe Pessoa: Crie uma classe que modele uma pessoa:

# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer. 
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__ (self, nome, idade, peso, altura):
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura

    def __str__(self):
        return f'nome: {self._nome} | idade: {self._idade} | peso: {self._peso} | altura: {self._altura}'
    
    def envelhecer(self):
        self._idade+=1
        self._crescer()
    
    def engordar(self,kg):
        self._peso += kg

    def _crescer(self):
        if self._idade <= 21:
            self._altura += 0.5