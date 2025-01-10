#lista = [10,8,7,5]
lista = []
soma = 0
tamanho_lista = len(lista)

try:
    for i in lista:
            soma += i
            print(f'Soma dos elementos: {soma}')
    else:
     print (soma / tamanho_lista)
except Exception as e:
      print(f'Ocorreu um erro: {e}')
