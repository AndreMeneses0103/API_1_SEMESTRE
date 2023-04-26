import json

with open ("Sprint3/data_json/turmas.json", 'r') as arquivo:
    dados = json.load(arquivo)

turmas= []

#seleciono somente as turmas
for turma in dados['turmas']:
    turmas.append(turma['nometurma'])
print(turmas)

#selecionar somente os times da turma escolhida
times = []
for turma in dados['turmas']:
    if turma['nometurma'] == 'Logistica':
        for time in turma['times']:
            times.append(time['nometime'])
print(times)
