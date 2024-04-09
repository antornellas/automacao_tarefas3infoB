from funcoes import login

while True:
    user = input('Digite o nome do usuário:')
    pwd = input('Digite a senha do usuário: ')
    if login(user,pwd):
        break
    else:
        print('Tente novamente!')