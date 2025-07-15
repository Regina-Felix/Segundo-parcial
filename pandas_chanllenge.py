import pandas as pd
import matplotlib.pyplot as plt

# Paso 1: Cargar la base de datos
datos = pd.read_csv('flights.csv')

# Mostrar las primeras filas
print("Primeras filas del archivo:")
print(datos.head())

# Paso 2: Revisar si hay datos faltantes
print("\nCantidad de datos faltantes por columna:")
print(datos.isnull().sum())

# Paso 3: Llenar valores faltantes en columnas de retraso con la media
# (Evita errores al hacer cálculos)
datos['DepDelay'].fillna(datos['DepDelay'].mean(), inplace=True)
datos['ArrDelay'].fillna(datos['ArrDelay'].mean(), inplace=True)

# Paso 4: Eliminar valores extremos (muy raros o atípicos)
# Solo vamos a mantener los retrasos que están entre -100 y 300 minutos
datos = datos[(datos['DepDelay'] > -100) & (datos['DepDelay'] < 300)]
datos = datos[(datos['ArrDelay'] > -100) & (datos['ArrDelay'] < 300)]

# Paso 5: Ver estadísticas básicas
print("\nEstadísticas generales:")
print(datos[['DepDelay', 'ArrDelay']].describe())

# Paso 6: Mostrar gráficas de los retrasos
plt.figure(figsize=(10, 4))

# Gráfico de retraso en salida
plt.subplot(1, 2, 1)
plt.hist(datos['DepDelay'], bins=40, color='skyblue')
plt.title('Retraso en salida')
plt.xlabel('Minutos')
plt.ylabel('Cantidad de vuelos')

# Gráfico de retraso en llegada
plt.subplot(1, 2, 2)
plt.hist(datos['ArrDelay'], bins=40, color='lightgreen')
plt.title('Retraso en llegada')
plt.xlabel('Minutos')

plt.tight_layout()
plt.show()

# Paso 7: Calcular el retraso promedio
print("\nPromedios de retraso:")
print("Promedio salida:", round(datos['DepDelay'].mean(), 2), "minutos")
print("Promedio llegada:", round(datos['ArrDelay'].mean(), 2), "minutos")

# Paso 8: Ver qué aerolínea tiene más retraso promedio en llegada
# Cambiar 'Aerolínea' por el nombre de la columna real para la aerolínea (ej. 'Carrier')
retraso_por_aerolinea = datos.groupby('Carrier')['ArrDelay'].mean().sort_values()
print("\nRetraso promedio por aerolínea:")
print(retraso_por_aerolinea)

# Paso 9: Ver retraso por día de la semana
# Asumiendo que la columna para el día de la semana es 'DayOfWeek'
retraso_por_dia = datos.groupby('DayOfWeek')['ArrDelay'].mean()
print("\nRetraso por día de la semana:")
print(retraso_por_dia)

# Paso 10: Aeropuerto con más retraso en salida
retraso_salida_aeropuerto = datos.groupby('OriginAirportName')['DepDelay'].mean().sort_values(ascending=False)
print("\nAeropuerto con más retraso promedio en salida:")
print(retraso_salida_aeropuerto.head(1))

# Paso 11: ¿Salir tarde causa llegar más tarde?
datos['SalidaTarde'] = datos['DepDelay'] > 0
print("\nPromedio de retraso en llegada según si salió tarde:")
print(datos.groupby('SalidaTarde')['ArrDelay'].mean())

# Paso 12: Crear la columna "Ruta" para analizar vuelos entre aeropuertos
datos['Ruta'] = datos['OriginAirportName'] + ' -> ' + datos['DestAirportName']

# Crear la columna 'ArrDelay15' para identificar llegadas con retraso de 15 minutos o más
datos['ArrDelay15'] = (datos['ArrDelay'] >= 15).astype(int)

# Ruta con más llegadas tarde
ruta_mas_tarde = datos[datos['ArrDelay15'] == 1]['Ruta'].value_counts().head(1)
print("\nRuta con más llegadas tarde:")
print(ruta_mas_tarde)

# Ruta con mayor retraso promedio de llegada
ruta_peor = datos.groupby('Ruta')['ArrDelay'].mean().sort_values(ascending=False).head(1)
print("\nRuta con mayor retraso promedio:")
print(ruta_peor)