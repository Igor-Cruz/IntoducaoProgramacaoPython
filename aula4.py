a = int(input('Primeiro Bimestre: '))
while a > 10:
    a = int(input('Você digitou errado: '))
b = int(input('Segundo Bimestre: '))
while b > 10:
    b = int(input('Você digitou errado: '))
c = int(input('Terceiro Bimestre: '))
while c > 10:
    c = int(input('Você digitou errado: '))
d = int(input('Quarto Bimestre: '))
while d > 10:
    d = int(input('Você digitou errado: '))
media = (a + b + c + d) / 4
if media >= 7 and media <=10:
    print('Parabéns você foi aprovado')
    print(' A média alcançada foi {}' .format(media))
elif media >= 4 and media < 7:
    print('Estude para a recuperação, sua média foi {}' .format(media))
else:
    print('Ano que vem estaremos juntos')



# a = int(input('Poderia digitar um n°: '))
#
# div = 0
# for x in range (1, a+1):
#     resto = a % x
#     print(x, resto)
#     if resto == 0:
#         div +=1
#         # div = div + 1
# if div == 2:
#     print('n° {} é primo' .format(a))
# else:
#     print('n° {} não é primo' .format(a))