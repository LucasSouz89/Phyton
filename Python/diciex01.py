pessoa = {
    'Carlos': {'nome': 'Carlos', 'cidade':'Guarulhos', 'idade':24},
    'Lucas': {'nome': 'Lucas', 'cidade':'Guarulhos', 'idade':24},
    'Everton':{'nome': 'Everton', 'cidade':'Camaquaa', 'idade':24},
    'Pedro':{'nome': 'Pedro', 'cidade':'Guarulhos', 'idade':23},
    'Alfredo' : {'nome': 'Alfredo', 'cidade':'Bragança','idade':27} }



pessoa['Everton']['idade'] = 25
pessoa['Everton']['Profissão'] = 'Desemprego'
pessoa['Everton'].pop('Profissão', None) 
for i in pessoa:
    print(pessoa)
    break


