import tkinter as tk
from tkinter import ttk
import datetime as dt

lista_tipos = ["GrupoA","GrupoB","GrupoC","GrupoD" ]
lista_codigos = []

janela = tk.Tk()

#Criação da Função

def inserir_codigo():
    descricao = entry_descricao.get()
    tipo = combobox_selecionar_tipo.get()
    data_criacao = dt.datetime.now()
    data_criacao = data_criacao.strftime("%d/%m/%y %H:%M")
    codigo = len(lista_codigos)+1
    codigo_str = "COD-{}".format(codigo)
    lista_codigos.append((codigo_str,descricao,tipo,data_criacao))


#Titulo da Janela

janela.title('Cadastro de Times')

label_descricao = tk.Label(text="Nome do Time")
label_descricao.grid(row=1, column=0, padx=10, pady=10, stick='nswe', columnspan =4 )

entry_descricao = tk.Entry()
entry_descricao.grid(row=2, column=0, padx=10, pady=10, stick='nswe', columnspan = 4)

label_tipo_unidade = tk.Label(text='Integrantes do Time')
label_tipo_unidade.grid(row=3, column=0, padx=10, pady=10, stick='nswe', columnspan =2)

combobox_selecionar_tipo = ttk.Combobox(values=lista_tipos)
combobox_selecionar_tipo.grid(row=3, column=2, padx=10, pady=10, stick='nswe', columnspan =2 )

botao_criar_codigo = tk.Button(text="Registrar Time", command=inserir_codigo)
botao_criar_codigo.grid(row=5,column=0,padx = 10, pady=10, sticky='nswe',columnspan =4)

janela.mainloop()

print(lista_codigos)
