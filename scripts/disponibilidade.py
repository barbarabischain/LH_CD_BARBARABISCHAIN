import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('indicium_precificacao.csv')
disp= df.groupby('bairro_group')['disponibilidade_365'].mean().sort_values()

print(disp)

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 6))
sns.barplot(
    x=disp.index,
    y=disp.values,
    palette='viridis'
)
plt.title('Disponibilidade Média por Região', fontsize=18)
plt.xlabel('Região', fontsize=16)
plt.ylabel('Disponibilidade Média (dias/ano)', fontsize=16)
plt.xticks(rotation=45, fontsize=14)
plt.savefig('disponibilidade_por_bairro.png', dpi=300, bbox_inches='tight')
