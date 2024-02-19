print('Digite sua idade: ')
idade = int (input())

if idade <= 12: 
    print('Você é uma criança.')
elif idade < 18:
    print ('Você é um adolescente.')  
elif idade <=64: 
    print ('Você é um adulto.')
else : 
    print ('Você é um idoso.')   

idade = int(idade) + 1
print('No ano que vem sua idade será', idade, '.')