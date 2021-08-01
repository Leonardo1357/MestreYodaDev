#Armazenando informações
print('Digite seu nome: ')
nome = input()

print('Digite o dia em que você nasceu: ')
dia = input()
print('Digite o mês em que você nasceu: ')
mês = input()
print('Digite o ano em que você nasceu: ')
ano = input()

data = dia + '/' + mês + '/' + ano

print('Bem vindo', nome + '.', 'Sua data de nascimento é', data)