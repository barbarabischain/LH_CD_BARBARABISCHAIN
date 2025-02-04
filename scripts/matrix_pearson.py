import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('indicium_precificacao_sem_outliers.csv')
colunas = ['price', 'minimo_noites', 'numero_de_reviews', 'disponibilidade_365',
            'reviews_por_mes', 'calculado_host_listings_count', 'latitude', 'longitude']
df_num = df[colunas].rename(columns={'calculado_host_listings_count': 'host_listing_count'})
df_num = df_num.dropna()
matrix_corr = df_num.corr(method='pearson')
plt.figure(figsize=(12, 8))
sns.heatmap(
    matrix_corr,
    annot=True,
    cmap='RdBu',
    vmin=-1,
    vmax=1,
    linewidths=0.5,
    annot_kws={"size": 14})
plt.xticks(rotation=44)
plt.title('Matriz: Pearson Correlação entre preço e outros fatores', fontsize=20)
plt.savefig('matriz_pearson.png', dpi=300, bbox_inches='tight')
