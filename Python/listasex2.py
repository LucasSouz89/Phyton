encomendas = input('Digite os números das encomendas separado por virgula').split(',')

try:
    for encomenda in encomendas:
        print(int(encomendas))
except ValueError:
    print('Uma das entradas não é um numero válido')