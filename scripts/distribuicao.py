import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

df = pd.read_csv('indicium_precificacao_sem_outliers.csv')
df_clean = df['price'].replace([np.inf, -np.inf], np.nan).dropna()

#Teste: Kolmogorov-Smirnov
ks_test = stats.kstest(df['price'], 'norm', args=(df['price'].mean(), df['price'].std()))
print('Kolmogorov-Smirnov Test Statistic:', ks_test.statistic)
print('Kolmogorov-Smirnov Test p-value:', ks_test.pvalue)

#Teste: Anderson-Darling
anderson_test = stats.anderson(df['price'], dist='norm')
print('Anderson-Darling Test Statistic:', anderson_test.statistic)
print('Anderson-Darling Critical Values:', anderson_test.critical_values)
print('Anderson-Darling Significance Levels:', anderson_test.significance_level)
stats.probplot(df['price'], dist="norm", plot=plt)
