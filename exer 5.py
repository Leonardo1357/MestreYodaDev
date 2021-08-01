
print('*************************************************************************')
print('Bem vindo, irei identificar se o que foi digitado contém apenas números, \nletras ou se é alfanúmerico.')
print('*************************************************************************')

frase = input('Digite aqui: ')

x = frase.isalpha()
z = frase.isdecimal()

if(x == True):
    print('Há apenas letras.')

elif(z == True):
    print('Há apaenas números.')

else:
    print('Contém números e letras, logo é alfanúmerico.')

print('Obrigago por testar!!')
