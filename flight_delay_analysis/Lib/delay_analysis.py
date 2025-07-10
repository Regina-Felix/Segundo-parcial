# src/delay_analysis.py

import pandas as pd
import matplotlib.pyplot as plt

def cargar_datos(ruta):
    """Carga el archivo CSV de vuelos"""
    return pd.read_csv(ruta)

def limpiar_datos(df):
    """Rellena valores nulos y elimina outliers"""
    df['DepDelay'] = df['DepDelay'].fillna(0)
    df['ArrDelay'] = df['ArrDelay'].fillna(0)
    df['DepDel15'] = df['DepDel15'].fillna(0)

    # Eliminar outliers
    for columna in ['DepDelay', 'ArrDelay']:
        Q1 = df[columna].quantile(0.25)
        Q3 = df[columna].quantile(0.75)
        IQR = Q3 - Q1
        df = df[(df[columna] >= Q1 - 1.5 * IQR) & (df[columna] <= Q3 + 1.5 * IQR)]

    return df

def mostrar_estadisticas(df):
    """Muestra estadísticas generales"""
    print("Estadísticas descriptivas:")
    print(df.describe())
    print(f"Promedio de retraso en salida: {df['DepDelay'].mean():.2f} min")
    print(f"Promedio de retraso en llegada: {df['ArrDelay'].mean():.2f} min")

def graficar(df):
    """Genera gráficos de análisis"""
    fig, axs = plt.subplots(2, 2, figsize=(14, 10))

    axs[0, 0].hist(df['DepDelay'], bins=50, color='skyblue', edgecolor='black')
    axs[0, 0].set_title('Distribución del Retraso de Salida')

    axs[0, 1].hist(df['ArrDelay'], bins=50, color='lightcoral', edgecolor='black')
    axs[0, 1].set_title('Distribución del Retraso de Llegada')

    delay_by_day = df.groupby('DayOfWeek')['ArrDelay'].mean()
    delay_by_day.plot(kind='bar', ax=axs[1, 0], color='orange')
    axs[1, 0].set_title('Retraso Promedio por Día')

    top_airports = df.groupby('OriginAirportName')['DepDelay'].mean().nlargest(10)
    top_airports.plot(kind='barh', ax=axs[1, 1], color='purple')
    axs[1, 1].set_title('Top 10 Aeropuertos con Mayor Retraso')
    axs[1, 1].invert_yaxis()

    plt.tight_layout()
    plt.show()

def main():
    df = cargar_datos('data/flights.csv')
    df = limpiar_datos(df)
    mostrar_estadisticas(df)
    graficar(df)

if __name__ == '__main__':
    main()
