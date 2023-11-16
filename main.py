import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


source = "inmuebles.csv"

df = pd.read_csv(source)

#LIMPIEZA
#----------------------------------------------------------------------------------------------------------
columnas = df.columns

columnas_mantener =['Tipo Inmueble', 'Ciudad', 'Departamento', 'Estrato', 'Valor Arriendo', 'Area Construida']

df_nuevo = df.drop(columns=[col for col in columnas if col not in columnas_mantener])

df_nuevo.dropna(inplace = True)

df_nuevo = df_nuevo.query("`Estrato` != 0 and `Area Construida` != 0")




#-----------------------------------------------------------------------------------------------------------
#QUITAR COMAS Y CAMBIAR EL TIPO DE DATOS DE CADA COLUMNA QUE DEBERIA SER NUMERICA

df_nuevo['Valor Arriendo'] = df_nuevo['Valor Arriendo'].str.replace(',', '')
df_nuevo['Area Construida'] = df_nuevo['Area Construida'].str.replace(',', '').astype(float).fillna(0).astype(int)

columnas_numericas = ['Estrato', 'Valor Arriendo', 'Area Construida']
df_nuevo[columnas_numericas] = df_nuevo[columnas_numericas].apply(pd.to_numeric, errors='coerce')



