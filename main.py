import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


source = "inmuebles.csv"

df = pd.read_csv(source)


columnas = df.columns

columnas_mantener =['Tipo Inmueble', 'Ciudad', 'Departamento', 'Estrato', 'Valor Arriendo', 'Area Construida']

df_nuevo = df.drop(columns=[col for col in columnas if col not in columnas_mantener])


#Para empezar la limpieza de los datos se clasifica cuales columnas son categoricas o numericas.   -----> #print(df_nuevo.dtypes)

#QUITAR COMAS Y CAMBIAR EL TIPO DE DATOS DE CADA COLUMNA QUE SE SUPONE QUE ES NUMERICA

df_nuevo['Valor Arriendo'] = df_nuevo['Valor Arriendo'].astype('str')
df_nuevo['Valor Arriendo'] = df_nuevo['Valor Arriendo'].str.replace(',', '')

df_nuevo['Valor Arriendo'] = df_nuevo['Valor Arriendo'].astype('int64')

columnas_numericas = ['Estrato', 'Valor Arriendo', 'Area Construida']
for columna in columnas_numericas:
    df_nuevo[columna] = pd.to_numeric(df_nuevo[columna], errors='coerce')

