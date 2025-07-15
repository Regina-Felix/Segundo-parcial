import pandas as pd
import matplotlib.pyplot as plt

# Paso 1: Cargar la base de datos
datos = pd.read_csv('flights.csv')

# Mostrar las primeras filas
print("Primeras filas del archivo:")
print(datos.head())

# Paso 2: Revisar datos faltantes
print("\nCantidad de datos faltantes por columna:")
print(datos.isnull().sum())

# Paso 3: Llenar valores faltantes en columnas de retraso con la media
for columna in ['DepDelay', 'ArrDelay']:
    datos[columna].fillna(datos[columna].mean(), inplace=True)

# Paso 4: Eliminar valores extremos (outliers)
# Mantener retrasos entre -100 y 300 minutos
datos = datos[(datos['DepDelay'].between(-100, 300)) & (datos['ArrDelay'].between(-100, 300))]

# Paso 5: Estadísticas básicas
print("\nEstadísticas generales de retrasos:")
print(datos[['DepDelay', 'ArrDelay']].describe())

# Paso 6: Visualizaciones básicas
plt.figure(figsize=(12, 6))

# Histograma de retraso en salida
plt.subplot(1, 2, 1)
plt.hist(datos['DepDelay'], bins=30, color='skyblue', alpha=0.8)
plt.title('Retraso en salida')
plt.xlabel('Minutos')
plt.ylabel('Cantidad de vuelos')

# Histograma de retraso en llegada
plt.subplot(1, 2, 2)
plt.hist(datos['ArrDelay'], bins=30, color='lightgreen', alpha=0.8)
plt.title('Retraso en llegada')
plt.xlabel('Minutos')
plt.ylabel('Cantidad de vuelos')

plt.tight_layout()
plt.show()

# Paso 7: Retraso promedio
print("\nPromedios de retraso:")
print(f"Promedio en salida: {datos['DepDelay'].mean():.2f} minutos")
print(f"Promedio en llegada: {datos['ArrDelay'].mean():.2f} minutos")

# Paso 8: Retraso promedio por aerolínea
retraso_por_aerolinea = datos.groupby('Carrier')['ArrDelay'].mean().sort_values(ascending=False)
print("\nRetraso promedio por aerolínea:")
print(retraso_por_aerolinea)

# Visualización: Retraso promedio por aerolínea
plt.figure(figsize=(12, 6))
retraso_por_aerolinea.plot(kind='bar', color='orange', alpha=0.7)
plt.title('Retraso promedio por aerolínea')
plt.xlabel('Aerolínea')
plt.ylabel('Retraso promedio (minutos)')
plt.xticks(rotation=45)
plt.show()

# Paso 9: Retraso promedio por día de la semana
retraso_por_dia = datos.groupby('DayOfWeek')['ArrDelay'].mean().sort_index()
print("\nRetraso promedio por día de la semana:")
print(retraso_por_dia)

# Visualización: Retraso promedio por día de la semana
dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
plt.figure(figsize=(10, 5))
plt.bar(dias, retraso_por_dia, color='purple', alpha=0.7)
plt.title('Retraso promedio por día de la semana')
plt.xlabel('Día de la semana')
plt.ylabel('Retraso promedio (minutos)')
plt.show()

# Paso 10: Aeropuerto con más retraso promedio en salida
retraso_salida_aeropuerto = datos.groupby('OriginAirportName')['DepDelay'].mean().sort_values(ascending=False)
print("\nAeropuerto con más retraso promedio en salida:")
print(retraso_salida_aeropuerto.head(5))

# Visualización: Aeropuertos con mayor retraso promedio en salida
plt.figure(figsize=(10, 5))
retraso_salida_aeropuerto.head(10).plot(kind='bar', color='red', alpha=0.8)
plt.title('Aeropuertos con más retraso promedio en salida')
plt.xlabel('Aeropuerto')
plt.ylabel('Retraso promedio (minutos)')
plt.xticks(rotation=45)
plt.show()

# Paso 11: Relación entre salida tarde y llegada tarde
datos['SalidaTarde'] = datos['DepDelay'] > 0
retraso_por_salida_tarde = datos.groupby('SalidaTarde')['ArrDelay'].mean()
print("\nPromedio de retraso en llegada según si salió tarde:")
print(retraso_por_salida_tarde)

# Visualización: Relación entre salida tarde y llegada tarde
plt.figure(figsize=(8, 4))
retraso_por_salida_tarde.plot(kind='bar', color=['green', 'blue'], alpha=0.7)
plt.title('Retraso en llegada según si salió tarde')
plt.xlabel('¿Salida tarde?')
plt.ylabel('Retraso promedio (minutos)')
plt.xticks([0, 1], ['No', 'Sí'], rotation=0)
plt.show()

# Paso 12: Análisis de rutas
datos['Ruta'] = datos['OriginAirportName'] + ' -> ' + datos['DestAirportName']
datos['ArrDelay15'] = (datos['ArrDelay'] >= 15).astype(int)

# Ruta con más llegadas tarde
ruta_mas_tarde = datos[datos['ArrDelay15'] == 1]['Ruta'].value_counts().head(1)
print("\nRuta con más llegadas tarde:")
print(ruta_mas_tarde)

# Ruta con mayor retraso promedio de llegada
ruta_peor = datos.groupby('Ruta')['ArrDelay'].mean().sort_values(ascending=False).head(1)
print("\nRuta con mayor retraso promedio:")
print(ruta_peor)

# Visualización: Rutas con mayor retraso promedio
top_rutas = datos.groupby('Ruta')['ArrDelay'].mean().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_rutas.plot(kind='bar', color='darkblue', alpha=0.8)
plt.title('Rutas con mayor retraso promedio')
plt.xlabel('Ruta')
plt.ylabel('Retraso promedio (minutos)')
plt.xticks(rotation=45)
plt.show()
