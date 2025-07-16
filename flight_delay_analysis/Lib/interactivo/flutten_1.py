import numpy as np
import matplotlib.pyplot as plt

# Simulamos una imagen 8x8 de un número "4" (matriz binaria)
numero_cuatro = np.array([
    [0, 0, 0, 1, 1, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
])

# Visualización de la matriz como imagen
plt.imshow(numero_cuatro, cmap='gray')
plt.title("Reconocimiento del número '4' (Matriz original)")
plt.show()

# Aplanamos la matriz con flatten (para usar en redes neuronales, por ejemplo)
numero_cuatro_aplanado = numero_cuatro.flatten()

print("Matriz aplanada (vector):\n", numero_cuatro_aplanado)
print("\nLongitud del vector aplanado:", len(numero_cuatro_aplanado))