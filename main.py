
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

print("¡Hola! Mi proyecto de Python funciona correctamente.")
print("Las 4 librerías se importaron correctamente.")

# PROYECTO: ANALISIS DE VENTAS

# Productos de nuestra tienda
productos = ["Relojes", "Pulseras", "Collares", "Anillos"]

# Cantidades vendidas
cantidades = np.array([15, 25, 12, 18])

# Precios de los productos
precios = np.array([150000, 35000, 60000, 45000])

# Calcular los ingresos de cada producto
ingresos = cantidades * precios

# Organizar los datos en una tabla
tabla = pd.DataFrame({
    "Producto": productos,
    "Cantidad": cantidades,
    "Ingresos": ingresos
})

# Mostrar resultados
print("\nVENTAS DE LA TIENDA")
print(tabla)

print("\nTotal vendido: $", np.sum(ingresos))

# Crear una grafica
sns.barplot(data=tabla, x="Producto", y="Ingresos")

plt.title("Analisis de ventas de la tienda")
plt.xlabel("Productos")
plt.ylabel("Ingresos en pesos")

# Guardar la grafica
plt.savefig("grafica_ventas.png")
print("\nGrafica creada correctamente.")
