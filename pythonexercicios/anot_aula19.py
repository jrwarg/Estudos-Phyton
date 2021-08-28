pessoas = {'nome': 'João', 'idade': 57, 'sexo': 'M'}
print(pessoas['nome'])
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"]}')
pessoas['nome'] = "Leandro"
pessoas['naturalidade'] = "brasileiro"
pessoas['peso'] = 57
for k, v in pessoas.items():
    print(f'{k} = {v}')

brasil = []
estado1 = {'uf': 'Rio de Janeiro'}
estado2 = {'uf': 'São Paulo'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)