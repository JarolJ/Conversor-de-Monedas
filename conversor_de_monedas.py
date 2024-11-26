import requests
import pandas as pd
import os

#Debes crearte una cuenta en https://app.exchangerate-api.com/ y obterer una API Key, son gratuitas
API_KEY = 'tu_clave_de_api'
URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/USD'

#Función para obtener la tasa de cambio mediante una llamada a la API
def obtener_tasas_de_cambio():
    response = requests.get(URL)
    data = response.json()
    if response.status_code != 200 or data['result'] != 'success':
        print("Error al obtener las tasas de cambio.")
        return None
    return data['conversion_rates']

#Función para obtener el valor de la cantidad convertida
def convertir_moneda(cantidad, moneda_origen, moneda_destino, tasas_de_cambio):
    if moneda_origen not in tasas_de_cambio or moneda_destino not in tasas_de_cambio:
        print("Moneda no soportada.")
        return None
    tasa_origen = tasas_de_cambio[moneda_origen]
    tasa_destino = tasas_de_cambio[moneda_destino]
    cantidad_convertida = (cantidad / tasa_origen) * tasa_destino
    return cantidad_convertida

#Función para guardar el historial de conversiones en un archivo EXCEL
def guardar_historial_en_excel(historial):
    nombre_archivo = 'historial_conversiones.xlsx'
    df = pd.DataFrame(historial)
    if os.path.exists(nombre_archivo):
        df_existente = pd.read_excel(nombre_archivo)
        df_final = pd.concat([df_existente, df], ignore_index=True)
        df_final.to_excel(nombre_archivo, index=False)
    else:
        df.to_excel(nombre_archivo, index=False)

#Función para obtener la entrada del usuario y llamar a las funciones pertinentes
def main():
    historial = []
    tasas_de_cambio = obtener_tasas_de_cambio()
    if tasas_de_cambio is None:
        return

    print("Bienvenido al conversor de monedas")
    while True:
        try:
            cantidad = float(input("Ingrese la cantidad de dinero que desea convertir: "))
            moneda_origen = input("Ingrese la moneda de origen (por ejemplo, USD, EUR): ").upper()
            moneda_destino = input("Ingrese la moneda de destino (por ejemplo, USD, EUR): ").upper()
            cantidad_convertida = convertir_moneda(cantidad, moneda_origen, moneda_destino, tasas_de_cambio)
            if cantidad_convertida is not None:
                print(f"{cantidad} {moneda_origen} son {cantidad_convertida:.2f} {moneda_destino}")
                historial.append({
                    "Cantidad": cantidad,
                    "Moneda Origen": moneda_origen,
                    "Moneda Destino": moneda_destino,
                    "Cantidad Convertida": cantidad_convertida
                })
            otra = input("¿Desea realizar otra conversión? (s/n): ").lower()
            if otra != 's':
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    guardar_historial_en_excel(historial)
    print("Historial de conversiones guardado en historial_conversiones.xlsx")

if __name__ == "__main__":
    main()
