import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


source = "inmuebles.csv"

data = pd.read_csv(source)

#Funciones
#----------------------------------------------------------------------------------------------------------

def quitar_tildes(texto):
    return unidecode.unidecode(texto)
#----------------------------------------------------------------------------------------------------------



#LIMPIEZA
#----------------------------------------------------------------------------------------------------------
columnas = data.columns

columnas_mantener =['Tipo Inmueble', 'Ciudad', 'Departamento', 'Estrato', 'Valor Arriendo', 'Area Construida']

#Nuevo data frame, nuevos nombre a las columnas

df_nuevo = data[columnas_mantener].copy().rename(columns={"Tipo Inmueble": "Inmueble", "Valor Arriendo": "Arriendo", "Area Construida": "Area"})



#NUEVO DATA FRAME----------------------------------------------------------------------------------------------------------


df_snc = df_nuevo.query("`Estrato` != 0 and `Area Construida` != 0")




#-----------------------------------------------------------------------------------------------------------
#QUITAR COMAS Y CAMBIAR EL TIPO DE DATOS DE CADA COLUMNA QUE DEBERIA SER NUMERICA

df_nuevo['Valor Arriendo'] = df_nuevo['Valor Arriendo'].str.replace(',', '')
df_nuevo['Area Construida'] = df_nuevo['Area Construida'].str.replace(',', '').astype(float).fillna(0).astype(int)

columnas_numericas = ['Estrato', 'Valor Arriendo', 'Area Construida']
df_nuevo[columnas_numericas] = df_nuevo[columnas_numericas].apply(pd.to_numeric, errors='coerce')





#---------------------------------------------------------------------------------------------------------------

#Modificando espacios, cortando nombres en la columna ciudad, quitando tildes
reemplazos = {
    "Bogotá D.C.": "Bogotá",
    "Cartagena de Indias": "Cartagena",
    "Guadalajara de Buga": "Buga"
}

# Realiza los reemplazos en la columna "Ciudad"
df_nuevo["Ciudad"].replace(reemplazos, inplace=True)

df_nuevo["Ciudad"] = df_nuevo["Ciudad"].apply(quitar_tildes)

#---------------------------------------------------------------------------------------------------------------
