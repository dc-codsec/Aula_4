carros_vendas = ['hb20', 'renegade', 'jimny', 'argo', 'gol']

tamanho_lista = len(carros_vendas)
print(tamanho_lista)

#in not in
if 'renegade' in carros_vendas:
    print('Sim')

if 'tracker' not in carros_vendas:
    print('Não')

carros_marcas = [
    ['polo', 'gol', 'virtus'],
    ['onix', 'tracker','monza']
]

print(carros_marcas[0][1])
carros_marcas[0][0] = 'fusca'
print(carros_marcas)
tamanho = len(carros_marcas)
print(tamanho)
print(carros_marcas[0])
tamanho = len(carros_marcas[0])
print(tamanho)

print(carros_vendas)
#acessar qq elemento lista posicao - 1 = indice
carros_vendas.append('Corcel')
print(carros_vendas)

carros_vendas.insert(0,'Onix')
print(carros_vendas)

del carros_vendas[0]
print(carros_vendas)

valor = carros_vendas.pop(1)
print(carros_vendas, valor)

carros_vendas.remove('argo')
print(carros_vendas)

numeros = [1,10,8,7,6,99]
print(sorted(numeros))
print(numeros)
numeros.sort()
print(numeros)
numeros.reverse()
print(numeros)

#URL = http://www.google.com.br
# x = 'aula'

#removam o http://
#lista com os demais componentes separados
#[www,google,com,br]

