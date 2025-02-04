import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tabulate import tabulate

df = pd.read_csv('indicium_precificacao_sem_outliers.csv')
print(df.info())
#pd.set_option('display.max_columns', None)
print(df.describe())

colunas = ['price', 'minimo_noites', 'numero_de_reviews', 'disponibilidade_365']
df_selecionado = df[colunas]
print(df_selecionado.describe())


#ESTATISTICA PARA CADA REGIAO (bairro_group)
stat_bairros = df.groupby('bairro_group')['price'].describe()
#stat_bairros.to_csv('tabela_preco_por_bairro.csv')
print(stat_bairros)

media_regiao = df.groupby('bairro_group')['price'].mean()
media_regiao = media_regiao.sort_values(ascending=False)

params = {
   'axes.labelsize': 20,
   'font.size': 20,
   'legend.fontsize': 20,
   'xtick.labelsize': 20,
   'ytick.labelsize': 20,
   'figure.figsize': [9, 6]
   }
plt.rcParams.update(params)

plt.figure(figsize=(12,6))
sns.barplot(x=media_regiao.index, y=media_regiao.values, palette='viridis')
plt.title('Preço médio por região (USD)')
plt.xlabel('Região')
plt.ylabel('Preço médio (USD)')
plt.xticks(rotation=40)
plt.show()
plt.savefig('preco_medio_regiao.png', dpi=300, bbox_inches='tight')
plt.close()
