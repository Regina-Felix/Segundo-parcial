import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parámetros del elipsoide (Tierra)
a = 1.0  # Semieje ecuatorial (normalizado)
b = 0.9966  # Semieje polar (aproximación del flattening 1/298)

# Crear una esfera de referencia para comparación
theta = np.linspace(0, 2*np.pi, 100)
phi = np.linspace(0, np.pi, 100)
theta, phi = np.meshgrid(theta, phi)

# Coordenadas esféricas para el elipsoide
x_ellipsoid = a * np.sin(phi) * np.cos(theta)
y_ellipsoid = a * np.sin(phi) * np.sin(theta)
z_ellipsoid = b * np.cos(phi)

# Coordenadas esféricas para la esfera perfecta (comparación)
x_sphere = a * np.sin(phi) * np.cos(theta)
y_sphere = a * np.sin(phi) * np.sin(theta)
z_sphere = a * np.cos(phi)

# Graficar
fig = plt.figure(figsize=(12, 6))

# Elipsoide achatado
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(x_ellipsoid, y_ellipsoid, z_ellipsoid, color='blue', alpha=0.7)
ax1.set_title('Elipsoide Achatado (Flattening)')

# Esfera perfecta (referencia)
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(x_sphere, y_sphere, z_sphere, color='red', alpha=0.7)
ax2.set_title('Esfera Perfecta')

plt.show()