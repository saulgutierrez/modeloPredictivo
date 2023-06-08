import pandas as pd
import matplotlib.pyplot as plt

workbook = "netflix_titles.csv"

df = pd.read_csv("netflix_titles.csv", nrows = 3, skiprows= range(1, 177)) # FILA 178-180

#print(df.head())

valores = df[["type", "title", "release_year", "rating", "duration"]]
#print(valores)

ax = valores.plot.bar(x = "title", y = "release_year", rot = 0)

plt.show()