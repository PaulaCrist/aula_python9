import json

lista = {
    'frutas': ['abacate', 'uva', 'kiwi'],
'data': '2023-05-20'
}

with open('arquivo.json' , 'w') as arquivo:
    json.dump(lista, arquivo)

meu_json = json.dumps(lista)

print(meu_json)