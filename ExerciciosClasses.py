from Classes.Bola import Bola
from Classes.Quadrado import Quadrado
from Classes.Retangulo import Retangulo
from Classes.Pessoa import Pessoa
from Classes.ContaCorrente import ContaCorrente

#ClasseBola
bolaQuadrada = Bola('azul','20 cm','plastico')

#ClasseQuadrado
quad = Quadrado(5)

#ClasseRetangulo
retangulo = Retangulo(5,10)

#ClassePessoa
pessoa = Pessoa('Laura',5,23.7,100)

#ClasseContaCorrente
conta1 = ContaCorrente('0251-9','Joana',40)


def main():
    i = -1
    while(i != 0):
        i = int(input('''
            DIGITE UM NUMERO PARA A OPÇÃO DESEJADA:
              1. Bola:
              2. Quadrado
              3. Retangulo
              4. Pessoa
              5. Conta corrente
              0. Sair
                      '''))
        
        # 6. TV
        #       7. Bichinho virtual
        #       8. Macaco
        #       9. Ponto e retangulo
        #       10. Bomba de combustivel

        if i == 1:
            print('1. Bola:')
            print(bolaQuadrada)
            bolaQuadrada.trocaCor('vermelha')
            print(bolaQuadrada.mostraCor())
            input()

        elif i == 2:
            print('2. Quadrado:')
            print(quad)
            print(quad.mudarValorLado(6))
            print(quad.calcularArea())
            input()

        elif i == 3:
            print('3. Retangulo:')
            print(retangulo)
            print(f'area: {retangulo.calcularArea()}')
            print(f'Perimetro: {retangulo.calcularPerimetro()}')
            area = input("Informe a area do local desejado: ")
            print(f'Quantidade necessaria: {retangulo.calculaQtdeRetangulos(area)}')
            input()
        elif i == 4:
            print('4. Pessoa:')
            print(pessoa)
            pessoa.envelhecer()
            pessoa.engordar(2)
            print(pessoa)
            input()
        elif i == 5:
            print('5. Conta corrente:')
            print(conta1)
            print(conta1.mudarNome('Joana Dark'))
            print(conta1.saque(50))
            print(conta1.deposito(90))
            print(conta1)
            input()
        # elif i == 6:
        #     pass
        # elif i == 7:
        #     pass
        # elif i == 8:
        #     pass
        # elif i == 9:
        #     pass
        # elif i == 10:
        #     pass
        else:
            'Digite um numero valido'

if __name__ == '__main__':
    main()