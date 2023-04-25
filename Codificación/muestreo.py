import numpy as np
import matplotlib.pyplot as plt

# Definir el tamaño de la población
tamano_poblacion = 100

# Crear una muestra aleatoria de tamaño 20
tamano_muestra = int(tamano_poblacion * 0.2) # 20% de la población
# Crea una lista de 20 numeros aleatorios entre 1 y 100
muestra_20 = np.random.choice(range(1, tamano_poblacion+1), tamano_muestra)

# Calcular la suma de la muestra
suma_muestra = np.sum(muestra_20)

# Estimacion de la muestra total
suma_estimada = suma_muestra * 5 # (tamaño_poblacion / tamaño_muestra)

# Imprimir los resultados
print("Suma real:", true_sum)
print("Suma de la muestra:", suma_muestra)
print("Estimación de la suma total:", suma_estimada)

# Crear un histograma de la muestra
plt.hist(muestra_20, bins=range(1, tamano_muestra+2), alpha=0.5)
plt.axvline(x=suma_muestra, color='g', linestyle='--', label='Suma de la muestra')
plt.axvline(x=suma_estimada, color='b', linestyle='--', label='Estimación de la suma total')
plt.legend()
plt.show()