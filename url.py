url = input('Digite uma url: ')
#http://
#www.site....
prefixo = url.removeprefix('http://') 
print(prefixo)
componentes = prefixo.split('.')
print(componentes)