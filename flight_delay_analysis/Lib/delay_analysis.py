# analisis_vuelos.py

import pandas as pd
import matplotlib.pyplot as plt
import os

# Carga el archivo CSV desde la ruta especificada
def cargar_datos(ruta):
    if not os.path.exists(ruta):
        print(f"Error: El archivo '{ruta}' no fue encontrado.")
        exit(1)
    return pd.read_csv(ruta)

# Rellena valores nulos y elimina outliers en las columnas de retraso
def limpiar_datos(df):
    df['DepDelay'] = df['DepDelay'].fillna(0)
    df['ArrDelay'] = df['ArrDelay'].fillna(0)
    df['DepDel15'] = df['DepDel15'].fillna(0)

    # Elimina valores atípicos usando el rango intercuartílico
    for columna in ['DepDelay', 'ArrDelay']:
        Q1 = df[columna].quantile(0.25)
        Q3 = df[columna].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[columna] >= Q1 - 1.5 * IQR) & (df[columna] <= Q3 + 1.5 * IQR)]

    return df

# Muestra estadísticas generales de los retrasos
def mostrar_estadisticas(df):
    print("\nEstadísticas Descriptivas:")
    print(df.describe())
    print(f"\nPromedio de retraso en salida: {df['DepDelay'].mean():.2f} minutos")
    print(f"Promedio de retraso en llegada: {df['ArrDelay'].mean():.2f} minutos")

# Genera gráficas de distribución y promedios por día y aeropuerto
def graficar(df):
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    axs[0, 0].hist(df['DepDelay'], bins=50, color='skyblue', edgecolor='black')
    axs[0, 0].set_title('Distribución del Retraso de Salida')
    axs[0, 0].set_xlabel('DepDelay')
    axs[0, 0].set_ylabel('Cantidad')

    axs[0, 1].hist(df['ArrDelay'], bins=50, color='lightcoral', edgecolor='black')
    axs[0, 1].set_title('Distribución del Retraso de Llegada')
    axs[0, 1].set_xlabel('ArrDelay')
    axs[0, 1].set_ylabel('Cantidad')

    delay_by_day = df.groupby('DayOfWeek')['ArrDelay'].mean()
    delay_by_day.plot(kind='bar', ax=axs[1, 0], color='orange')
    axs[1, 0].set_title('Retraso Promedio por Día de la Semana')
    axs[1, 0].set_xlabel('Día de la Semana (1=Lunes)')
    axs[1, 0].set_ylabel('Minutos de Retraso')
    axs[1, 0].grid(axis='y')

    top_airports = df.groupby('OriginAirportName')['DepDelay'].mean().nlargest(10)
    top_airports.plot(kind='barh', ax=axs[1, 1], color='purple')
    axs[1, 1].set_title('Top 10 Aeropuertos con Mayor Retraso Promedio')
    axs[1, 1].set_xlabel('Minutos de Retraso')
    axs[1, 1].set_ylabel('Aeropuerto')
    axs[1, 1].invert_yaxis()
    axs[1, 1].grid(axis='x')

    plt.tight_layout()
    plt.show()

# Realiza análisis complementarios del dataset
def analisis_avanzado(df):
    print("\nRetraso promedio por aerolínea:")
    print(df.groupby('Carrier')['ArrDelay'].mean().sort_values())

    print("\nRetraso promedio por día de la semana (1=Lunes, 7=Domingo):")
    print(df.groupby('DayOfWeek')['ArrDelay'].mean())

    origin_delay = df.groupby('OriginAirportName')['DepDelay'].mean().sort_values(ascending=False)
    print("\nAeropuerto con mayor retraso promedio en salida:")
    print(origin_delay.head(1))

    late_departures = df[df['DepDelay'] > 15]
    on_time_departures = df[df['DepDelay'] <= 0]

    print(f"\nPromedio de retraso en llegada si el vuelo salió tarde: {late_departures['ArrDelay'].mean():.2f} minutos")
    print(f"Promedio de retraso en llegada si el vuelo salió a tiempo: {on_time_departures['ArrDelay'].mean():.2f} minutos")

    df['Route'] = df['OriginAirportName'] + " → " + df['DestAirportName']
    late_arrivals = df[df['ArrDelay'] > 15]

    print(f"\nRuta con más llegadas tarde: {late_arrivals['Route'].value_counts().idxmax()}")
    print("Ruta con mayor retraso promedio en llegada:")
    print(df.groupby('Route')['ArrDelay'].mean().sort_values(ascending=False).head(1))

# Función principal del programa
def main():
    df = cargar_datos('flights.csv')  # Asegúrate de que flights.csv está en la misma carpeta
    df = limpiar_datos(df)
    mostrar_estadisticas(df)
    graficar(df)
    analisis_avanzado(df)

# Punto de entrada del script
if __name__ == '__main__':
    main()
