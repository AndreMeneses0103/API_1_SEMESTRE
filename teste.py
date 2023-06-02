import matplotlib.pyplot as plt

# Dados para o eixo x e y
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Plotar a linha
plt.plot(x, y, 'r-')  # 'r-' define a cor e o estilo da linha (vermelho)

# Plotar os pontos
plt.scatter(x, y, c='b')  # 'c' define a cor dos pontos (azul)

# Adicionar rótulos aos pontos
for i, j in zip(x, y):
    plt.text(i, j, f'({i}, {j})')

# Exibir o gráfico
plt.show()
