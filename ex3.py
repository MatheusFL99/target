import json

with open ('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

# menor e maior
dia_menor_valor = dia_maior_valor = dados[0]['dia']
valor_menor = valor_maior = dados[0]['valor']

for dado in dados:
    if dado['valor'] < valor_menor:
        dia_menor_valor = dado['dia']
        valor_menor = dado['valor']
    elif dado['valor'] > valor_maior:
        dia_maior_valor = dado['dia']
        valor_maior = dado['valor']

# media e dias maiores q a media
valor_soma = 0
for faturamento in dados:
  valor_soma += faturamento['valor']
media = valor_soma / len(dados)

nmaiorq_media = 0
for dado in dados:
    if dado['valor'] > media:
        nmaiorq_media += 1



print('Dia com menor valor: Dia', dia_menor_valor)
print('Dia com maior valor: Dia', dia_maior_valor)
print('Número de dias em que o valor foi maior que a média:', nmaiorq_media)



