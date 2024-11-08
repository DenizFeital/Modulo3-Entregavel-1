import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Definindo a área de plotagem
plt.figure(figsize=(10, 6))
# Dados de exemplo
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 8, 12, 11, 11, 9, 13, 15, 14, 12]
# Criando o gráfico com os eixos x e y
plt.plot(x, y, label='Ações da empresa XYZ')
# Configurando as propriedades do gráfico
plt.xlabel('Dia')
plt.ylabel('Valor')
plt.title('Gráfico de Linha com Matplotlib')
plt.legend()
plt.grid(True)
plt.xticks(x) # Definindo os valores do eixo x
# Exibindo o gráfico
plt.show()

# Definindo a área de plotagem
plt.figure(figsize=(12, 6))
# Dados de exemplo
categorias = ['A', 'B', 'C', 'D', 'E', 'F']
valores = [10, 20, 15, 30, 25, 22]
# Gráfico de barras
plt.bar(categorias, valores, color='orange')
# Configurando as propriedades do gráfico
plt.xlabel('Categoria')
plt.ylabel('Valor')
plt.title('Gráfico de Barras')
# Exibindo o gráfico
plt.show()

# Definindo a área de plotagem
plt.figure(figsize=(4, 4))
# Dados de exemplo
ids = ['A', 'B', 'C', 'D']
valores = [15, 30, 45, 10]
cores = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
# Criar o gráfico de pizza
plt.pie(valores, labels=ids, colors=cores, autopct='%1.1f%%')
# Adicionar título
plt.title('Gráfico de Pizza')
# Mostrar o gráfico
plt.show()

