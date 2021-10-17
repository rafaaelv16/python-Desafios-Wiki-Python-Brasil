# 3 - Faça um Programa que verifique se uma letra digitada é "F" ou "M".
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = input('Digite o sexo: F ou M ')
f_m = 'Sexo Inválido'

if sexo == 'M':
    f_m = 'M - Masculino'

elif sexo == 'F':
    f_m = 'F - Feminino'

print(f_m)




