import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

df = pd.read_csv('indicium_precificacao_sem_outliers.csv')

features = ['bairro_group', 'bairro', 'latitude', 'longitude', 'room_type',
           'minimo_noites', 'calculado_host_listings_count', 'disponibilidade_365']

X = df[features]
y = df['price']

le_bairro_group = LabelEncoder()
le_bairro = LabelEncoder()
le_room = LabelEncoder()

X['bairro_group'] = le_bairro_group.fit_transform(X['bairro_group'])
X['bairro'] = le_bairro.fit_transform(X['bairro'])
X['room_type'] = le_room.fit_transform(X['room_type'])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
sgd_model = SGDRegressor(max_iter=10000, tol=1e-5, random_state=42)
sgd_model.fit(X_train, y_train)

y_pred = sgd_model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('SGDRegressor Performance:')
print(f'Mean Absolute Error: ${mae:.2f}')
print(f'Root Mean Squared Error: ${np.sqrt(mse):.2f}')
print(f'R² Score: {r2:.3f}')
print(f'y_pred: {y_pred}')
print(f'average price: {y_test.mean()}')

skylit = {'bairro_group': 'Manhattan',
 'bairro': 'Midtown',
 'latitude': 40.75362,
 'longitude': -73.98377,
 'room_type': 'Entire home/apt',
 'minimo_noites': 1,
 'calculado_host_listings_count': 2,
 'disponibilidade_365': 355}
skil = pd.DataFrame([skylit])

skil['bairro_group'] = le_bairro_group.transform(skil['bairro_group'])
skil['bairro'] = le_bairro.transform(skil['bairro'])
skil['room_type'] = le_room.transform(skil['room_type'])

skil = scaler.fit_transform(skil)

print(f'preço: {sgd_model.predict(skil)}')
