'''Crie um programa que calcule o valor total das compras de um cliente. O
programa deve solicitar indefinidamente que o usuário digite o preço de
cada produto adquirido. Quando o usuário digitar a tecla 'igual' no lugar
do preço do produto, o programa deve exibir a soma dos preços de todos
os produtos digitados.'''

soma = 0
while True:
    print ('Digite o preço de cada produto adquirido:')
    valor=(input())
    if (valor == '=') :
        print('A soma dos produtos é:',soma)
        break  
    else:
        soma= soma + valor  
        break