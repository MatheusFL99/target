import json

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

with open ('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

valor_soma = 0
for faturamento in dados:
  valor_soma += faturamento['valor']

print(f"O porcentual de SP sobre o valor total mensal foi de: {(sp/valor_soma*100):.2f}% ")
print(f"O porcentual de RJ sobre o valor total mensal foi de: {(rj/valor_soma*100):.2f}% ")
print(f"O porcentual de MG sobre o valor total mensal foi de: {(mg/valor_soma*100):.2f}% ")
print(f"O porcentual de ES sobre o valor total mensal foi de: {(es/valor_soma*100):.2f}% ")
print(f"O porcentual de outros estados sobre o valor total mensal foi de: {(outros/valor_soma*100):.2f}% ")