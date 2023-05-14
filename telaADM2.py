import json
with open("data_json/turmas.json", "r") as arquivo:
    dados = json.load(arquivo)

    for x in range(len(dados['turmas'])):
        print(x)
        ordem = x

    ordem +=1