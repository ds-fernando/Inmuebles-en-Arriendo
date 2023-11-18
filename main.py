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
df_nuevo = df_nuevo[df_nuevo['Inmueble'] != 'Isla'].copy()



#-----------------------------------------------------------------------------------------------------------
#QUITAR COMAS Y CAMBIAR EL TIPO DE DATOS DE CADA COLUMNA QUE DEBERIA SER NUMERICA

df_nuevo['Valor Arriendo'] = df_nuevo['Valor Arriendo'].str.replace(',', '')
df_nuevo['Area Construida'] = df_nuevo['Area Construida'].str.replace(',', '').astype(float).fillna(0).astype(int)

columnas_numericas = ['Estrato', 'Valor Arriendo', 'Area Construida']
df_nuevo[columnas_numericas] = df_nuevo[columnas_numericas].apply(pd.to_numeric, errors='coerce')
df_ia = df_nuevo.query("~Inmueble.isna()")



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
#Creacion de DataFrames


df_rentabilidad = df_ia[["Inmueble", "Arriendo"]]

df_sin_nulos = df_nuevo.dropna().copy()


valores_a_excluir = ['Oficina', 'Local Comercial', 'Deposito', 'Garaje', 'Consultorio', 'Parqueadero Privado', 'Bodega', 'Edificacion para Hotel - Motel']

df_calidad= df_sin_nulos[~df_nuevo['Inmueble'].isin(valores_a_excluir)].copy()