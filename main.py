import pandas as pd
import numpy as np
import matplotlib.pyplot
import matplotlib


source = "inmuebles.csv"

df = pd.read_csv(source)

#Para empezar la limpieza de los datos se clasifica cuales columnas son categoricas o numericas. 
# Tipo inmueble = categorica
# Ciudad = Categorica
#Departamento = categorica
#Area construida =numerica 
#Valor arriendo = numerica
#codigo sae = numerica
#estrato = numerica




columnas= list(df.columns)  ##Revisando las columnas
columnas_mantener =['Tipo Inmueble', 'Ciudad', 'Departamento', 'Estrato', 'Valor Arriendo', 'Area Construida']


df_nuevo = df.drop(columns=[col for col in columnas if col not in columnas_mantener])


print(df_nuevo.columns)


