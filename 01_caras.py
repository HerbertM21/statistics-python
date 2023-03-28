import numpy as np
import matplotlib.pyplot as plt

n_experiments = 1200
results = []

caras = 0
for experiment in range(n_experiments):
    monedas = np.random.randint(0, 2, size=2)
    caras += np.sum(monedas == 1)
    longitud = len(monedas)
    # Formula proporción = caras / (numeros de lanzamientos * numero de experimento actual) 
    # Formula proporción = caras / (longitud de la muestra * numero de experimento actual + 1) (empieza desde 0, por eso) 
    proporción = caras / (longitud * (experiment + 1))
    results.append(proporción)

# LEY DE LOS GRANDES NÚMEROS
mean_results = np.mean(results)
print('Ley de los grandes números: ', mean_results)

# Graficar los resultados
# Graficar los resultados de todos los experimentos juntos
# plt.plot(10, [lista de proporciones de cara], '-o')
plt.plot(range(1, n_experiments+1), results, '-o')
plt.title('Proporción de caras en lanzamiento de moneda')
plt.axhline(mean_results, color='r', linestyle='--', label='Ley de los grandes números')
plt.xlabel('Experimentos')
plt.ylabel('Proporción de caras')
plt.ylim([0, 1])
plt.xlim([0, n_experiments+1])
plt.legend()
plt.show()

# La convergencia de 0.5 en una distribucion binomial se refiere a la probabilidad de que salga cara en una moneda, 
# es decir, 0.5. En este caso, la ley de los grandes numeros nos dice que la proporción de caras en cada experimento
# se acerca a 0.5 conforme aumenta el numero de experimentos.

# ES IMPORTANTE QUE LA LEY DE GRANDES NUMEROS NO SE DESCARTA QUE ALGUNOS RESULTADOS SEAN MUY DISTINTO A SU CONVERGENCIA
# SIEMPRE LOS PRIMEROS EXPERIMENTOS SON LOS QUE MAS SE DESVIAN DE LA CONVERGENCIA
# LOS QUE ESTAN MAS CERCA DE LA CONVERGENCIA SON LOS ULTIMOS EXPERIMENTOS