meu_dicionario = {'Lucas':{'nome':'Lucas','idade':'24','profissão':'programador'}}

chave_verificação = 'idade'


if chave_verificação in meu_dicionario['Lucas']:
 print(f'Idade esta inserido no codigo')
else:
 print(f'Idade não esta inserido no codigo')