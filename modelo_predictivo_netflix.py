import numpy as np
import matplotlib.pyplot as plt

# Periods (1920-1929, 1930-1939, 1940-1949, 1950-1959, 1960-1969, 1970- 1979, 1980- 1989, 1990-1999, 2000-2009, 2010-2019, 2020-)
x = np.array([1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020])
y = np.array([1, 0, 14, 11, 25, 70, 129, 274, 810, 5927, 1545])

anno = 2030
coef = np.polyfit(x, y, 3)
p = np.polyval(coef, anno)
print(f"Para el año {anno} la predicción es {p}")

def fx (x1, coef):
    fx = 0
    n = len(coef) - 1
    for p in coef:
        fx = fx + p * x1**n
        n = n - 1
    return fx

x1 = np.linspace(1920, anno + 1, 1000)
y1 = fx(x1, coef) # funcion
plt.figure(figsize=[20, 10])
plt.title("Cantidad de peliculas producidas por década")

# En el grafico, la recta representa la predicción, mientras que los puntos representan los datos

plt.scatter(x, y, s=120, c='blueviolet')
plt.plot(x1, y1, "--", linewidth=3, color = 'orange')
plt.scatter(anno, p, s=200, c='red')
plt.yticks(range(0, 6000, 1000))
plt.grid("on")
ax = plt.gca()
ax.set_xlabel("$años$")
ax.set_ylabel("$Cantidad peliculas$")
plt.show()