#Classe Bola: Crie uma classe que modele uma bola:

#Atributos: Cor, circunferência, material
#Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self,cor,circunferencia,material):
        self._cor = cor
        self._circunferencia = circunferencia
        self._material = material

    def __str__(self):
        return f'cor: {self._cor} | circunferencia: {self._circunferencia} | material: {self._material}'
    
    def trocaCor(self,cor):
        self._cor = cor

    def mostraCor(self):
        return f'A cor é {self._cor}'

#bolaQuadrada = Bola('azul','20 cm','plastico')
#bolaQuadrada.cor = 'azul'
#bolaQuadrada.circunferencia='20 cm'
#bolaQuadrada.material = 'plastico'
#print(dir(bolaQuadrada))
#print(vars(bolaQuadrada))
#print(bolaQuadrada)
#bolaQuadrada.trocaCor('vermelha')
#print(bolaQuadrada.mostraCor())

