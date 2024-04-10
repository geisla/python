#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

''' numero = int(input("Insira um numero: "))

if numero % 2 == 0:
    print("O numero é PAR")
else: 
    print("O numero é IMPAR") '''



#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

#Criança: 0 a 12 anos;
#Adolescente: 13 a 18 anos;
#Adulto: acima de 18 anos.
    
'''idade = int(input("Insira a sua idade: "))

if 0 < idade <= 12:
    print("Criança: 0 a 12 anos")
elif 13 >= idade <=18:
    print("Adolescente: 13 a 18 anos")
elif idade > 18:
    print("Adulto: acima de 18 anos.")'''



#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

'''user = "gecatron"
senha = "123"

usu = input("Usuario: ")
passwd = input("Senha: ")

if usu != user or passwd != senha: 
    print("Acesso negado") 
else:
    print("Acesso concedido")'''

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.


'''coord_x = float(input("Diite o ponto de coordenada X: "))
coord_y = float(input("Diite o ponto de coordenada Y: "))

if coord_x > 0 and coord_y > 0:
    print("Primeiro Quadrante")
elif coord_x < 0 and coord_y > 0:
    print("Segundo Quadrante")
elif coord_x < 0 and coord_y < 0:
    print("Terceiro Quadrante")
elif coord_x > 0 and coord_y < 0:
    print("Quarto Quadrante")
else: 
    print("O ponto está localizado no eixo ou origem.")'''