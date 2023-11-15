#importar bibliotecas necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Abrir archivo para trabajar
df = pd.read_csv('2017_Yellow_Taxi_Trip_Data.csv')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

#Obtener info de los datos
df.info()
#Observar tabla
print(df.describe())

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Ordenar por la columna 'trip_distance' en orden descendente
df_sorted_trip = df.sort_values(by='trip_distance', ascending=False)

# Guardar la tabla ordenada por 'trip_distance' en un nuevo archivo CSV
df_sorted_trip.to_csv('sorted_by_trip_distance.csv', index=False)

# Ordenar por la columna 'total_amount' en orden descendente
df_sorted_total = df.sort_values(by='total_amount', ascending=False)

# Guardar la tabla ordenada por 'total_amount' en un nuevo archivo CSV
df_sorted_total.to_csv('sorted_by_total_amount.csv', index=False)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def filtro_tipo_de_pago(num_tipo):
    # Filtrar el DataFrame
    df_payment_type = df[df['payment_type'] == num_tipo]

    # Calcular el promedio de las columnas relevantes para el pago
    avg_payment_type = df_payment_type[['trip_distance', 'total_amount']].mean()

    # Imprimir el promedio para payment_type
    if num_tipo == 1:
        tipo_de_pago = "con tarjeta"
    elif num_tipo == 2:
        tipo_de_pago = "con efectivo"
    elif num_tipo == 3:
        tipo_de_pago = "sin cargo"
    elif num_tipo == 4:
        tipo_de_pago = "en disputa"
    elif num_tipo == 5:
        tipo_de_pago = "desconocido"
    elif num_tipo == 6:
        tipo_de_pago = "cancelado"

    print("\nPromedio para viajes pagados " + tipo_de_pago)
    print(avg_payment_type)

    # Pie chart
    labels = ['trip_distance', 'total_amount']
    values = avg_payment_type.values
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title(f'Promedio para viajes pagados {tipo_de_pago}')
    plt.show()

for pago in range(1, 5):
    filtro_tipo_de_pago(pago)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Contar las ocurrencias de cada vendor ID
vendor_counts = df['VendorID'].value_counts()

# Imprimir el conteo de vendor IDs
print("\nConteo de vendor IDs:")
print(vendor_counts)

# Calcular el promedio del total_amount para cada VendorID
mean_total_amount_per_vendor = df.groupby('VendorID')['total_amount'].mean()

# Imprimir el resultado
print("\nPromedio del 'total_amount' para cada 'vendor_id':")
print(mean_total_amount_per_vendor)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Filtrar el DataFrame para incluir solo pagos con tarjeta de crédito
df_credit_card = df[df['payment_type'] == 1]

# Calcular el promedio del tip_amount para cada passenger_count
average_tip_per_passenger_count = df_credit_card.groupby('passenger_count')['tip_amount'].mean()

# Imprimir el resultado
print("\nPromedio del tip_amount para cada passenger_count (pagos con tarjeta de crédito):")
print(average_tip_per_passenger_count)

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Calcular el promedio del tip_amount para cada vendor_id
average_tip_per_vendor = df.groupby('VendorID')['tip_amount'].mean()

# Imprimir el resultado
print("\nPromedio del 'tip_amount' para cada 'vendor_id':")
print(average_tip_per_vendor)