# Conversor-de-Monedas

Este proyecto es un **Conversor de Monedas** escrito en Python. Utiliza la API de [ExchangeRate-API](https://www.exchangerate-api.com/) para obtener tasas de cambio actualizadas y permite convertir entre diferentes monedas. Además, el historial de conversiones se guarda en un archivo Excel para un seguimiento fácil.

## Características

- **Conversión de Monedas**: Convierte entre diferentes monedas utilizando tasas de cambio actualizadas.
- **Entrada del Usuario**: El usuario puede especificar la cantidad y las monedas de origen y destino.
- **Historial de Conversiones**: Guarda todas las conversiones realizadas en un archivo Excel (`historial_conversiones.xlsx`).

## Requisitos

- Python 3.x
- Bibliotecas: `requests`, `pandas`, `openpyxl`

## Instalación

1. Clona este repositorio:
   ```sh
   git clone https://github.com/JarolJ/Conversor-de-Monedas.git
   ```
2. Navega al directorio del proyecto:
   ```sh
   cd Conversor-de-Monedas
   ```
3. Instala las dependencias necesarias:
   ```sh
   pip install requests pandas openpyxl
   ```

## Uso

1. Asegúrate de tener una clave de API de [ExchangeRate-API](https://www.exchangerate-api.com/) y reemplaza `tu_clave_de_api` en el código.
2. Ejecuta el script:
   ```sh
   python conversor_monedas.py
   ```

## Ejemplo

```sh
Ingrese la cantidad de dinero que desea convertir: 100
Ingrese la moneda de origen (por ejemplo, USD, EUR): USD
Ingrese la moneda de destino (por ejemplo, USD, EUR): EUR
100 USD son 91.25 EUR
¿Desea realizar otra conversión? (s/n): n
Historial de conversiones guardado en historial_conversiones.xlsx
```

## Contribuciones

Las contribuciones son bienvenidas. Siéntete libre de abrir issues y pull requests para mejorar este proyecto.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.
```
