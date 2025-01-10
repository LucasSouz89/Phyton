lista_valores = [15,20,25,30]
soma_valores = 0

try:
  for numero in lista_valores:
    soma_valores += numero
    print(f'Soma dos elementos: {soma_valores}')
except Exception as e:
  print(f'Ocorreu um erro: {e}')