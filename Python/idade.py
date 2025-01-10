import os
def perguntar_idade():
 idade_requirida = int(input('Insira uma idade: '))
 if  0 <= idade_requirida <= 12:
  print(' Você é criança')
 elif  13 <= idade_requirida < 18:
  print(' Você é adolecente')
 elif idade_requirida >= 18 :
  print(' Você é adulto')
 else:
  print('Insira uma idade válida')



def main():
  perguntar_idade()

if __name__ == '__main__':
 main()
