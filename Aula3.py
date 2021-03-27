a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Você digitou errado: '))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Você digitou errado: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Você digitou errado: '))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Você digitou errado: '))
media = (a + b + c + d) / 4
if media >= 7 and media <=10:
    print('Parabéns você foi aprovado')
    print(' A média alcançada foi {}' .format(media))
elif media >= 4 and media < 7:
    print('Estude para a recuperação, sua média foi {}' .format(media))
else:
    print('Ano que vem estaremos juntos')

# a = int(input('Digite o primeiro n°: '))
# b = int(input('Digite o segundo n°'))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('Foi digitado um n° é par: ')
# else:
#     print('Não foi digitado nenhum n° é impar:')

# a = int(input('Primeiro valor é: '))
# b = int(input('Segundo valor é: '))
# c = int(input('O Terceiro valor é: '))
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}' .format(b))
# else:
#     print('O maior valor é {}' .format(c))
# print('Obrigado pela sua contribuição.')

