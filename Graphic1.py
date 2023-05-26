import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

def f(x, y):
    L = 10.0
    V = 5.0
    result = (V * x / L)
    for n in range(1,4000):   
            result += ((2 * V) / np.pi) * ((-1.0) ** n)/n * (np.sin((n * np.pi * x)* (1/L))) * (np.exp((-n * np.pi * y) / L))
    return result

# Crear los valores de x e y
x = np.linspace(0, 10, 50)
y = np.linspace(0, 30, 50)
X, Y = np.meshgrid(x, y)

# Calcular los valores de la función para cada par de (x, y)
Z = f(X, Y)

# Crear la figura y el gráfico en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Graficar la superficie
ax.plot_surface(X, Y, Z, cmap='viridis')

# Etiquetas de los ejes
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('\u03A6 (x,y)')

# Título del gráfico
title= '\u03A6'+r"(x,y) = $\frac{2V}{\pi} \sum_{n=1}^{4000} \frac{(-1)^{n}}{n} \sin{(\frac{n \pi x}{L})} e^{\frac{-n \pi y}{L}} + \frac{Vx}{L}$"+"\n L=10 \n V=5"
ax.set_title(title, loc='center', y=1)




# Mostrar el gráfico
plt.show()