import os

os.system('cls')

def usuario_senha():
 usuario = input('Insira um nome de usuario')
 senha = int(input('Senha:'))

 if usuario == 'lucas' and senha == 123:
  print('Bem vindo!')
 else:
  print('Usuario não encontrado')

def main():
  usuario_senha()

if __name__ == '__main__':
    main()



