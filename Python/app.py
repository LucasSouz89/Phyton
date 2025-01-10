import os

restaurantes = [{'nome':'Praça', 'categoria':'Japonesa','ativo':False},
                {'nome':'Pizza Suprema', 'categoria':'Italiana','ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano','ativo':False}]


def exibir_nome_do_programa():
  print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
╚█████╗░███████║██████╦╝██║░░██║██████╔╝
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝

███████╗██╗░░██╗██████╗░██████╗░███████╗███████╗░██████╗
██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
█████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░█████╗░░╚█████╗░
██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░██╔══╝░░░╚═══██╗
███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗███████╗██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░""")

def exibir_opcao():
  '''Função que exibe as opções'''
  print('1.Cadastrar restaurante')
  print('2.Listar restaurantes')
  print('3.Alternar estado do restaurante')
  print('4.Sair\n')

def opcao_invalida():
 print('Opção invalida!\n')
 voltar_ao_menu()

def exibir_subtitulo(texto):
  '''Função que exibi o subtitulo'''
  os.system('cls')
  linha = '*' * (len(texto))
  print (linha)
  print (texto)
  print (linha)
  print()

def cadastrar_novo_restaurante():
  ''' Essa função  é responsalvel por cadastrar um novo restaurante
  
  Inputs:
  -Inserir nome de restaurante
  -Categoria restaurante
  
  Output:
  - Adiciona um restaurante a lista de restaurantes
  
  '''
  exibir_subtitulo('Cadastrar novo restaurantes')
  nome_do_restaurante = input ('Insira um nome de restaurante: ')
  categoria_do_restaurante = input ('Insira uma categoria para o restaurante: ')
  dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria_do_restaurante, 'ativo':False}
  restaurantes.append(dados_do_restaurante)
  print(f'O restaurante ' + nome_do_restaurante + ' foi cadastrado com sucesso!')
  voltar_ao_menu()

def listar_restaurantes():
  ''' Essa função  é responsalvel por listar os restaurante'''

  exibir_subtitulo('Listar Restaurante')
  print (f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Estado')
  for restaurante in restaurantes:
    nome_restaurante = restaurante['nome']
    categoria = restaurante ['categoria']
    ativo = 'ativado' if restaurante ['ativo'] else 'desativado'
    print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}' )
  voltar_ao_menu()

def estado_restaurante():
  '''Essa função exibe o estado do restaurante'''
  exibir_subtitulo('Alternar o estado do restuarante')
  nome_restaurante = input('Digite o nome do restaurante que deseja alternar o estado ')
  restaurantes_encontrado = False
  for restaurante in restaurantes:
    if nome_restaurante == restaurante['nome']:
      restaurantes_encontrado = True
      restaurante['ativo'] != restaurante ['ativo']
      mensagem = f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['ativo'] else f'O restaurante foi desativado com sucesso'
      print(mensagem)
  if not restaurantes_encontrado:
    print('O restaurante não foi encontrado')
  
  voltar_ao_menu()


def escolher_opcao():
  '''Função que escolhe a opção'''
  try:
    opcao_escolhida = int(input('Escolha uma opção: '))
    
    print(type(opcao_escolhida))
    if opcao_escolhida == 1:
      cadastrar_novo_restaurante()
    elif opcao_escolhida == 2:
      listar_restaurantes()
    elif opcao_escolhida == 3:
      estado_restaurante()
    elif opcao_escolhida == 4:
      finalizar_app()
    else:
      opcao_invalida()
  except:
    opcao_invalida()



def voltar_ao_menu():
  input('\nDigite qualquer tecla para voltar ao menu:')
  main()



def finalizar_app():
  exibir_subtitulo('Finalizar app')



def main():
  os.system('cls')
  exibir_nome_do_programa()
  exibir_opcao()
  escolher_opcao()
  
  
if __name__ == '__main__':
  main()