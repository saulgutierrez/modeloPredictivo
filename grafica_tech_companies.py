import pandas as pd
import matplotlib.pyplot as plt

workbook = "tech_companies.csv"

df = pd.read_csv("tech_companies.csv", nrows = 7)

# print(df.head())

valores = df[["Company Name", "Founding Year", "Employee Size"]]
# print(valores)

valores.plot.bar(x = "Company Name", y = "Employee Size", rot = 0)

plt.show()