'''
Exercicio 3:
Crie um programa que execute repetidamente o programa do exercício 2. 
Após a apresentação do resultado o programa deve perguntar se o usuário
deseja continuar a calcular, se a resposta for S(Sim) o programa deve 
continuar. Se a respota for N(Não),deve terminar.
'''
while True:
    
    print('Digite um número:')
    n1= float(input())
    print('Digite mais um número:')
    n2= float(input())
    print('Digite um operador básico matemático que deseja: + para soma,- para subtração,* para multiplicação e / para divisão.')
    operador= (input())

    if operador == ('+') :
        soma=n1 + n2
        print('Resultado da soma:', soma)
    elif operador == ('-') :
        subtração=n1 - n2
        print('Resultado da subtração:', subtração)
    elif operador == ('*') :
        multiplicação=n1 * n2
        print('Resultado da multiplicação:', multiplicação)
    else:  
        divisão=n1 / n21
        print('Resultado da divisão:', divisão)        
        break

    print ('Deseja continuar calculando? Responda S para Sim e N para Não.')   
    cont= (input()) 
    if (cont == 'N' or cont =='n') :
        break