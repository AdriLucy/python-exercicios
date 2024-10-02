# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. 
# Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos necessárias para o local.

class Retangulo:
    def __init__(self,comprimento,largura):
        self._comprimentocomprimento = comprimento
        self._largura = largura

    def __str__(self):
        return f'L: {self._largura} | C: {self.comprimento}'
    
    def calcularArea(self):
        area = self.comprimento * self._largura
        return area

    def calcularPerimetro(self):
        perimetro = 2*(self._largura+self.comprimento)
        return perimetro
    
    def calculaQtdeRetangulos(self,areaInformada):
        qtde = int(areaInformada)/self.calcularArea()
        return qtde