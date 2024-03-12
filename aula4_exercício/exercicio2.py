'''
Exercício 2:
Crie um programa que recebe 2 números reais como entrada e um
operador matemático. De acordo com o operador matemático fornecido
o programa deve calcular e apresentar o resultado da operação.
Exemplo de entrada: 
1.2 + ; 2.3
Exemplo Saída: O reusltado da soma é 3.5
'''

#entradas
print('Digite um número:')
n1= float(input())
print('Digite mais um número:')
n2= float(input())
print('Digite um operador básico matemático que deseja: + para soma,- para subtração,* para multiplicação e / para divisão.')
operador= (input())

#processamento
if operador == ('+') :
    soma=n1 + n2
    print('Resultado da soma:', soma)
elif operador == ('-') :
    subtração=n1 - n2
    print('Resultado da subtração:', subtração)
elif operador == ('*') :
    multiplicação=n1 * n2
    print('Resultado da multiplicação:', multiplicação)
elif operador == ('/') :    
    divisão=n1 / n2
    print('Resultado da divisão:', divisão)       
else:
    print('Operador desconhecido')
