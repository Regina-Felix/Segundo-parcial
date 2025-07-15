import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
df_flights = pd.read_csv('flights.csv')

# Mostrar las primeras filas del dataset
print("Primeras filas del dataset:")
print(df_flights.head())

# Verificar valores nulos antes de la limpieza
print("\nValores nulos antes de la limpieza:")
print(df_flights.isnull().sum())

# Eliminar filas con valores nulos
df_flights = df_flights.dropna()

# Establecer límites razonables para los retrasos
max_delay = 300  # máximo retraso en minutos
df_flights = df_flights[(df_flights['DepDelay'] <= max_delay) & (df_flights['ArrDelay'] <= max_delay)]

# Verificar el resultado de la limpieza
print("\nDatos después de la limpieza:")
print(df_flights.head())

# Verificar valores nulos después de la limpieza
print("\nValores nulos después de la limpieza:")
print(df_flights.isnull().sum())

# Rastreo de los índices después de la limpieza
df_flights.reset_index(drop=True, inplace=True)

# Resumen estadístico de las columnas numéricas
print("\nResumen estadístico del dataset:")
print(df_flights.describe())

# Distribución de los retrasos de salida (DepDelay)
plt.figure(figsize=(10, 6))
sns.histplot(df_flights['DepDelay'], bins=50, kde=True, color='blue')
plt.title('Distribución de los retrasos de salida (DepDelay)')
plt.xlabel('Retraso de salida (minutos)')
plt.ylabel('Frecuencia')
plt.show()

# Distribución de los retrasos de llegada (ArrDelay)
plt.figure(figsize=(10, 6))
sns.histplot(df_flights['ArrDelay'], bins=50, kde=True, color='red')
plt.title('Distribución de los retrasos de llegada (ArrDelay)')
plt.xlabel('Retraso de llegada (minutos)')
plt.ylabel('Frecuencia')
plt.show()

# Promedio de los retrasos de llegada por día de la semana
df_flights['DayOfWeek'] = df_flights['DayOfWeek'].astype('category')
average_delay_by_day = df_flights.groupby('DayOfWeek')['ArrDelay'].mean()

# Visualizar el promedio de los retrasos por día de la semana
plt.figure(figsize=(10, 6))
average_delay_by_day.plot(kind='bar', color='green')
plt.title('Promedio de los retrasos de llegada por día de la semana')
plt.xlabel('Día de la semana')
plt.ylabel('Retraso promedio de llegada (minutos)')
plt.xticks(rotation=0)
plt.show()

# Promedio de los retrasos de llegada por aerolínea
average_delay_by_carrier = df_flights.groupby('Carrier')['ArrDelay'].mean()

# Visualizar el promedio de los retrasos por aerolínea
plt.figure(figsize=(10, 6))
average_delay_by_carrier.plot(kind='bar', color='purple')
plt.title('Promedio de los retrasos de llegada por aerolínea')
plt.xlabel('Aerolínea (Carrier)')
plt.ylabel('Retraso promedio de llegada (minutos)')
plt.xticks(rotation=45)
plt.show()

# Agrupar por origen y destino y calcular el retraso medio de llegada
route_delay = df_flights.groupby(['OriginAirportName', 'DestAirportName'])['ArrDelay'].mean()


# Mostrar las 10 rutas con más retrasos de llegada
top_10_routes = route_delay.sort_values(ascending=False).head(10)
print("\nTop 10 rutas con más retrasos de llegada:")
print(top_10_routes)

# Promedio de retraso por aerolínea  (nuevo calculo)
average_delay_by_carrier = df_flights.groupby('Carrier')['ArrDelay'].mean().sort_values(ascending=False)

# Resultado (nuevo)
print("\nPromedio de retraso por aerolínea (de mayor a menor):")
print(average_delay_by_carrier)


# Correlación entre los retrasos de salida y llegada
plt.figure(figsize=(10, 6))
sns.scatterplot(x='DepDelay', y='ArrDelay', data=df_flights, color='orange')
plt.title('Correlación entre los retrasos de salida y llegada')
plt.xlabel('Retraso de salida (minutos)')
plt.ylabel('Retraso de llegada (minutos)')
plt.show()

# Calcular el coeficiente de correlación
correlation = df_flights['DepDelay'].corr(df_flights['ArrDelay'])
print(f"\nCoeficiente de correlación entre los retrasos de salida y llegada: {correlation}")

