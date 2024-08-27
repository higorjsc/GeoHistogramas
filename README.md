# Histograma Interativo


Este script Python gera histogramas interativos a partir de dados em uma coluna de um arquivo CSV. Ele produz três tipos de gráficos:

* **Histograma de Barras:** Exibe a distribuição de frequência dos dados em barras.
* **Histograma Acumulado:** Mostra a frequência acumulada dos dados.
* **Probability Plot:** Plota os dados ordenados contra suas respectivas probabilidades, auxiliando na análise da distribuição.


## Requisitos


* Python 3.x
* Bibliotecas: `pandas`, `matplotlib`, `numpy`, `argparse`, `scipy`


## Como Usar


1. **Instale as dependências:**

   ```bash
   pip install pandas matplotlib numpy scipy

2. **Execute o script via linha de comando:**

    ```bash
    python nome_do_script.py -I caminho/para/seu/arquivo.csv -V nome_da_coluna -D delimitador_do_csv -N codigo_na_value -P prefixo_desejado
* `-I` ou `--input`: Caminho para o arquivo CSV contendo os dados.
* `-V` ou `--var`: Nome da coluna que você deseja analisar.
* `-D` ou `--delimiter`: Caractere delimitador usado no seu arquivo CSV (padrão='-99.00').
* `-N` ou `--na_code`: Opcional - Código de valor não atribuído (padrão=',').
* `-P` ou `--prefix`: Opcional - Prefixo para os nomes dos arquivos de imagem gerados.

3. **Visualize os gráficos: Os gráficos serão salvos como arquivos PNG com os nomes:**

* `prefixo_desejado`-HistBars.png
* `prefixo_desejado`-HistAcum.png
* `prefixo_desejado`-ProbPlt.png


## Exemplo de Uso


1. Execute o prompt de comando (cmd)
2. Navegue até a pasta que contém o script `histos.py` e o csv `ferro.csv`
3. Insira o comando: <code>python histos.py -I ferro.csv -V Fe -P Grafico_Ferro</code>
