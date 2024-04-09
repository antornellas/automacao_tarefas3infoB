'''
As funções são utilizadas para modularizar o código, ou seja,
dividí-lo em partes menores, que podem ser reutilizadas.

Estrutura:

def noe_funcao(param1, param2):
    faz algo
    return valor

Exemplos:
'''
#Função 1
def somar(n1,n2):
    resultado= n1+n2
    return resultado


#Função 2:
def login(usuario, senha):
    if usuario == 'admin' and senha == '123':
        return True
    else:
        return False


#Função 3:
def calcularAreaTriangulo (base,altura):
    area= (base * altura)/2
    return area              

#Chamar Função
'''
print(login("ivan","123"))

area= calcularAreaTriangulo(100,50)
print('A área do triângulo é', area)
'''