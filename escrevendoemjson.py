import json

with open ('Sprint3/data_json/turmas.json', "r") as turmas:
    data_turma = json.load(turmas)

novos_dados = data_turma
#dados simulados, mas na implementação os valores atribuidos as variaveis serão as reais
idturma = "bancodedados123"#usar 1+
nometurma = "Gestão"
sprints = [{"indice":"4", 
            "inicioSprint": "12/12/2023",
            "fimSprint":"12/12/2023"
            }]
times = [
    {
            "idtime": "1234",
            "nometime": "TechHorizon",
            "quantidadeIntegrantes": 8,
            "integrantes":[{ }]
    },
    {
            "idtime": "124",
            "nometime": "DevTudo",
            "quantidadeIntegrantes": 10,
            "integrantes":[{ }]
    }
            ]


dados_novos ={
        "idturma": idturma,
        "nometurma": nometurma,
        "sprints": sprints,
        "times": times   
}

novos_dados['turmas'].append(dados_novos)
novos_dados = json.dumps(novos_dados, indent=4)


with open ("Sprint3/data_json/turmas.json" , "w") as escrevendo:
    escrevendo.write(novos_dados)
