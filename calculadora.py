def calcular():
    operacao = input('''
Qual operação você gostaria de fazer?
somar, subtrair, multiplicar ou dividir.     
''')

    numero_1 = int(input("Digite um número: "))
    numero_2 = int(input("Digite outro número: "))


    if operacao == "somar":
        print(numero_1 + numero_2)
    elif operacao == "subtrair":
        print(numero_1 - numero_2)
    elif operacao == "dividir":
        print(numero_1 / numero_2)
    elif operacao == "multiplicar":
        print(numero_1 * numero_2)
    else:
        print("Você escreveu algo errado!")

    novamente()

def novamente():
    calc_novamente = input('''
Você quer calcular novamente?
Precione S para sim e N para não.
''')
    
    if calc_novamente.upper() == 'S':
        calcular()
    elif calc_novamente.upper() == 'N':
        print('Até mais!')
    else:
        novamente()
        
calcular()