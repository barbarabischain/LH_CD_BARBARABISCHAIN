import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('indicium_precificacao.csv')

def find_outliers(df, coluna):
    q1 = df[coluna].quantile(0.25)
    q3 = df[coluna].quantile(0.75)
    iqr = q3 - q1
    lim_inf = q1 - 1.5 * iqr
    lim_sup = q3 + 1.5 * iqr
    outliers = df[(df[coluna] < lim_inf) | (df[coluna] > lim_sup)]
    return outliers

groups = df.groupby(['bairro_group', 'room_type'])
outliers_groups = {}
# for group_name, data_group in groups:
#     outliers = find_outliers(data_group, 'price')
#     outliers_groups[group_name] = outliers
# for group_name, outliers in outliers_groups.items():
#     print(group_name)
#     print(outliers[['price', 'minimo_noites']])
#     print('\n')

#criar nova tabela sem os outliers
df_new = df.copy()

for group_name, data_group in groups:
    outliers_rm = find_outliers(data_group, 'price')
    df_new.loc[outliers_rm.index, 'price'] = None

df_new = df_new.dropna(subset=['price'])
df_new.to_csv('indicium_precificacao_sem_outliers.csv', index=False)
plt.figure(figsize=(12, 5))
