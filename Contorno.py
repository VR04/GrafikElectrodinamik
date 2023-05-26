import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    L = 10.0
    V = 5.0
    result = (V * x / L)
    for n in range(1,4000):
        result += ((2 * V) / np.pi) * ((-1.0) ** n)/n * (np.sin(n * np.pi * x / L)) * (np.exp(-n * np.pi * y / L))
    return result

# Crear los valores de x e y
x = np.linspace(0, 10, 50)
y = np.linspace(0, 30, 50)
X, Y = np.meshgrid(x, y)

# Calcular los valores de la función para cada par de (x, y)
Z = f(X, Y)

# Crear la figura y el gráfico en 2D
fig = plt.figure()
ax = fig.add_subplot(111)

# Graficar la función como una imagen
image = ax.imshow(Z, extent=[x.min(), x.max(), y.min(), y.max()], origin='lower', cmap='viridis')

# Agregar una barra de colores
cbar = plt.colorbar(image)

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')

ax.set_aspect('auto')

# Título del gráfico
ax.set_title('Gráfico de f(X, Y) en el plano XY')

# Mostrar el gráfico
plt.show()