"""
not
V = F
F = V
"""


numero = float(input('Digite um numero um par: '))
par = False

if numero % 2 == 0:
    par = True

if not par:
    print(f'{numero} impar')
else:
    print('Continua execução')

# if numero == 0:
#     print('0')
# elif numero > 0:
#     print('positivo')
# else:
#     print('negativo')

# if not numero:
#     print('valor digitado é zero')
# else:
#     print(f'{numero} é positivo' if numero > 0 else f'{numero} é negativo')








