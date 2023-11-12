import pandas as pd
import numpy as np
import matplotlib.pyplot
import matplotlib


source = "inmuebles.csv"

df = pd.read_csv(source)


columnas= list(df.columns)  ##Revisando las columnas
columnas_mantener =['Codigo SAE', 'Tipo Inmueble', 'Ciudad', 'Departamento', 'Estrato', 'Valor Arriendo', 'Area Construida']


df_nuevo = df.drop(columns=[col for col in columnas if col not in columnas_mantener])

