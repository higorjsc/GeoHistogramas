import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse
from scipy import stats
from scipy.interpolate import interp1d

# ARGS
####################################################################

parser = argparse.ArgumentParser(description='Gera histogramas interativos do tipo: barras, acumulado e proability plot')
parser.add_argument('-I','--input', type=str, help='Caminho do arquivo .csv input') 
parser.add_argument('-V','--var', type=str, help='Nome da coluna/variável de interesse')
parser.add_argument('-P','--prefix', type=str, help='Prefixo para o nome das imagens output')
parser.add_argument('-D','--delimiter', type=str, default=",", help="Opcional - Caracter delimitador do arquivo .csv (padrão=',')")
parser.add_argument('-N','--na_code', type=float, default=-99.00, help="Opcional - Código de valor não atribuído (padrão=-99.00)")
args = parser.parse_args()

# INPUTS
####################################################################

#Geral
file_path = args.input  # Certifique-se de que o caminho do arquivo esteja correto
coluna = args.var
outputNamePrefix = args.prefix + "-" # Nome das figuras de output = outputPrefix + tipoGrafico
xTituloEixo = coluna
csvDelimiter = args.delimiter

# Histograma
yTituloEixoHist= "Frequência Acumulada (%)"
tituloGraficoHist = 'Histograma'

# Histograma Acumulado
yTituloEixoHistAcum = "Frequência Acumulada (%)"
tituloGraficoHistAcum = 'Histograma Acumulado'

# Probability Plot
yTituloEixoHistPlt = "Probabilidade (%)"
tituloGraficoHistPlt = 'Probability Plot'


# LEITURA DE DADOS
#################################################################

# Ler o arquivo CSV
df = pd.read_csv(file_path, delimiter=csvDelimiter, na_values=-99.00)
dados = df[coluna].dropna()


# HISTOGRAMA DE BARRAS
#################################################################

#Cálculos
tipoGraficoHist = "HistBars"
contagem, bins = np.histogram(dados, bins=30)
hist_acumulado = np.cumsum(contagem)
hist_acumulado_percent = hist_acumulado / hist_acumulado[-1] * 100

# Calcular a média e mediana
media = np.mean(dados)
mediana = np.median(dados)

# Criar função de interpolação para os dados do histograma
interpolation_function = interp1d(bins[:-1], hist_acumulado_percent, kind='linear', bounds_error=False, fill_value='extrapolate')

# Calcular as frequências percentuais a partir do histograma acumulado
frequencias_percentuais = np.diff(hist_acumulado_percent, prepend=0)

# Plotar o histograma de barras em frequência percentual
plt.figure(figsize=(10, 6))
plt.bar(bins[:-1], frequencias_percentuais, width=np.diff(bins), align='edge', color='skyblue', edgecolor='black')

# Adicionar labels e título
plt.xlabel(xTituloEixo)
plt.ylabel(yTituloEixoHist) 
plt.title(tituloGraficoHist)
plt.grid(axis='y', alpha=0.75)

# Adicionando linhas de referência (opcional)
plt.axvline(x=mediana, color='g', linestyle='--', linewidth=1, label=f'Mediana ({mediana:.2f})')
plt.axvline(x=media, color='purple', linestyle='--', linewidth=1, label=f'Média ({media:.2f})')

# Adicionando a legenda
plt.legend()

# Mostrar o gráfico
plt.savefig(outputNamePrefix + tipoGraficoHist)  # Salva como PNG


# HISTOGRAMA ACUMULADO
#################################################################

# Cálculos
tipoGraficoHistAcum = "HistAcum"
contagem, bins = np.histogram(dados, bins=30)
hist_acumulado = np.cumsum(contagem)
hist_acumulado_percent = hist_acumulado / hist_acumulado[-1] * 100

# Calcular a média e mediana
media = np.mean(dados)
mediana = np.median(dados)

# Criar função de interpolação para os dados do histograma
interpolation_function = interp1d(bins[:-1], hist_acumulado_percent, kind='linear', bounds_error=False, fill_value='extrapolate')

# Plotar o histograma acumulado
plt.figure(figsize=(10, 6))
plt.plot(bins[:-1], hist_acumulado_percent, color='blue', linestyle='-', linewidth=2, marker='o', markersize=5)

# Adicionando labels e título
plt.xlabel(xTituloEixo)
plt.ylabel(yTituloEixoHistAcum)
plt.title(tituloGraficoHistAcum)
plt.grid(True)

# Adicionando linhas de referência
plt.axvline(x=mediana, color='g', linestyle='--', linewidth=1, label=f'Mediana ({mediana:.2f})')
plt.axvline(x=media, color='purple', linestyle='--', linewidth=1, label=f'Média ({media:.2f})')

# Adicionando a legenda
plt.legend()

# Mostrar o gráfico
plt.savefig(outputNamePrefix + tipoGraficoHistAcum)  # Salva como PNG

# PROBABILITY PLOT
#################################################################

# Cálculos
tipoGraficoProbPlt = "ProbPlt"
dados_ordenados = np.sort(dados)
probabilidades = (np.arange(len(dados_ordenados)) + 0.5) / len(dados_ordenados)

# Plotar o gráfico de probabilidade
plt.figure(figsize=(10, 6))
plt.plot(dados_ordenados, probabilidades * 100, marker='o', linestyle='none', color='blue')  # Multiplica por 100 para ter a escala em %

# Adicionando labels e título
plt.xlabel(xTituloEixo)
plt.ylabel(yTituloEixoHistPlt)
plt.title(tituloGraficoHistPlt)
plt.grid(True)

# Definir limites do eixo y de 0 a 100
xMin = np.min(dados_ordenados) - np.min(dados_ordenados) * 0.1
xMax = np.max(dados_ordenados) + np.max(dados_ordenados) * 0.05
plt.xlim(xMin, xMax)
plt.ylim(-1, 102)
 
# Mostrar o gráfico
plt.savefig(outputNamePrefix + tipoGraficoProbPlt)  # Salva como PNG
