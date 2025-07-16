import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Cargar los datos
df = pd.read_csv('flights.csv')

# Convertimos datos útiles
df['Cancelled'] = df['Cancelled'].astype(bool)
df['Delayed'] = df['DepDelay'] > 15

# --- 1. Conteo de vuelos por mes ---
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Month', palette='coolwarm')
plt.title('Número de vuelos por mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad de vuelos')
plt.grid(True)
plt.show()

# --- 2. Porcentaje de vuelos cancelados por aerolínea ---
cancelled_by_carrier = df.groupby('Carrier')['Cancelled'].mean().sort_values(ascending=False) * 100

plt.figure(figsize=(12, 6))
cancelled_by_carrier.plot(kind='bar', color='red')
plt.title('Porcentaje de vuelos cancelados por aerolínea')
plt.ylabel('% Cancelados')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# --- 3. Mapa de calor de retrasos por aeropuerto de origen ---
delay_avg = df.groupby('OriginAirportName')['DepDelay'].mean().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=delay_avg.values, y=delay_avg.index, palette='magma')
plt.title('Aeropuertos con mayor retraso promedio de salida')
plt.xlabel('Retraso promedio (min)')
plt.ylabel('Aeropuerto')
plt.show()

# --- 4. Visualización interactiva con Plotly: Vuelos por ciudad de origen ---
fig = px.histogram(df, x='OriginCity', color='Cancelled',
                   title='Vuelos por ciudad de origen (coloreado por cancelación)',
                   labels={'Cancelled': 'Cancelado'}, barmode='group')
fig.update_layout(xaxis_title='Ciudad de origen', yaxis_title='Número de vuelos')
fig.show()
