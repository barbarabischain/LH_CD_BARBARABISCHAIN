import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('indicium_precificacao_sem_outliers.csv')
regiao = df['bairro_group'].unique()
plt.rcParams.update({'font.size': 20})

for i in regiao:
    dados_bairro = df[df['bairro_group'] == i]

    plt.figure(figsize=(12, 6))
    sns.histplot(
        data=dados_bairro,
        x='price',
        hue='room_type',
        kde=True,
        palette='viridis',
        bins=30,
        multiple='stack',
    )
    plt.title(f'{i}')
    plt.xlabel('Preço (USD)')
    plt.ylabel('Frequência')
    plt.savefig(f'histograma_preco_{i.replace(" ", "_")}.png', dpi=300, bbox_inches='tight')
    plt.close()
    