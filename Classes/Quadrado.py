#Classe Quadrado: Crie uma classe que modele um quadrado:

#Atributos: Tamanho do lado
#Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self,tamanhoDoLado):
        self._tamanhoDoLado = int(tamanhoDoLado)

    def __str__(self):
        return f'lado: {self._tamanhoDoLado}'
    
    def mudarValorLado(self,lado):
        self._tamanhoDoLado = lado
        return f'novo lado: {self._tamanhoDoLado}'

    def calcularArea(self):
        return self._tamanhoDoLado ** 2