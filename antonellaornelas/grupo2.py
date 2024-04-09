'''Crie um programa que imprima mensagens motivacionais dependendo do
horário do dia. O programa deve solicitar a hora atual. Se a hora estiver
entre 8 e 10, o programa deve imprimir “Bom dia! Você consegue alcançar
seus objetivos!”. Se a hora estiver entre 10 e 149,99, imprimir “Hora do almoço!
Recarregue suas energias para continuar avançando!”. Se estiver entre 14
e 17, imprimir “Boa tarde! Persista nos seus esforços, você está no caminho
certo!”.'''

print('Digite o horário atual:')
horas= int(input())

if (horas >=8) & (horas<10):
    print('Bom dia! Você consegue alcançar seus objetivos!')

elif (horas >=10) & (horas<14) :
    print('Hora do almoço! Recarregue suas energias para continuar avançando!') 

elif (horas >=14) & (horas<=17) :
    print('Boa tarde! Persista nos seus esforços, você está no caminho certo!')   

else:
    print('Não há mensagem disponível!')    