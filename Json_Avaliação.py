import json
#data ['dados_avaliação']['nome'] = 'Maria'

with open('C\Users\Lucas\Documents\GitHub\API_1_SEMESTRE\questions.json', 'r') as f:
    data = json.load(f)

exem1 = data

data ['dados_avaliacao']['nome'] = 'Maria'
data ['dados_avaliacao']['resposta1'] = '1'
data ['dados_avaliacao']['resposta2'] = '2'
data ['dados_avaliacao']['resposta3'] = '3'
data ['dados_avaliacao']['resposta4'] = '4'
data ['dados_avaliacao']['resposta5'] = '5'

dados_avaliacao = {
    "nome":avaliado,
    "resposta1":resposta1,
    "resposta2":resposta2,
    "resposta3":resposta3,
    "resposta4":resposta4,
    "resposta5":resposta5
}
exem1['Avaliados'].append(dados_avaliacao)
exem1 = json.dumps(exem1, indent=4)

with open('C\Users\Lucas\Documents\GitHub\API_1_SEMESTRE\questions.json', 'w') as r:
    r.write(exem1)



