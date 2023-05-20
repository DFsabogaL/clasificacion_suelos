import pandas as pd
import numpy as np
import matplotlib.pyplot as plt  # Se importo las librerias que permiten realizar graficos y realizar calculos 
import math


limite_liquido=0                  #Se establecen las variables de forma global 
limite_plastico=0
indice_plasticidad=0
coeficiente_uniformidad=0
coeficiente_cuervatura=0


tamiz = pd.Series([              # Se crea una serie utilizando la libreria de pandas, una serie se puede considerar un vector o una lista de datos 
    '3/4"',
    '1/2"',
    '3/8"',
    'No.4',
    'No.10',
    'No.40',
    'No.200',
    'Fondo',
])                                # La serie de tamices corresponde a la serie utilizada regularmente en el laboratorio de suelos de la Universidad Distriral Francisco jose de Caldas 

diametro_tamiz=pd.Series([
    19,      # Diamtro tamiz 3/4
    12.5,    # Diamtro tamiz 1/2
    9.5,     # Diamtro tamiz 3/8
    4.75,    # Diamtro tamiz No.4
    2,       # Diamtro tamiz No.10
    0.425,   # Diamtro tamiz No.40
    0.075,   # Diamtro tamiz No.200
    0,       # Fondo, no contiene valor 
    
])           # Si se cambia la serie de tamices, se deben asignar los diametros correspondientes, consulte en  (https://www.utest.com.tr/upload/Node/26142/xfiles/Testing-Sieves-IMPORTS-ES+1.pdf)

peso_retenido =pd.Series([
    0,       #Ingrese el peso en gramos retenido en el tamiz 3/4
    0,       #Ingrese el peso en gramos retenido en el tamiz 1/2
    0,       #Ingrese el peso en gramos retenido en el tamiz 3/8
    20,      #Ingrese el peso en gramos retenido en el tamiz No.4
    74,      #Ingrese el peso en gramos retenido en el tamiz No.10
    370,     #Ingrese el peso en gramos retenido en el tamiz No.40
    133,     #Ingrese el peso en gramos retenido en el tamiz No.200
    131,     #Ingrese el peso en gramos, que quedo en el fondo de la serie de tamices 
])


peso_retenido.sum()

TablaGranulometrica = pd.DataFrame({         # Se utiliza la libreria de panda para crear un DataFrame, que es un base da datos, funciona como los diccionarios de python 
    'Tamiz':tamiz,
    'Diametro (mm)':  diametro_tamiz,
    'Peso Retenido(gr)' : peso_retenido,     # Se pone el nombre de la columna y la variable de la serie creada anteriormente
    
     
})           

TablaGranulometrica['% Retenido']=peso_retenido*100/peso_retenido.sum()                      # Se estan agragando columnas al Data Frame, la columna de % Retenido se calcula apartir de la Columna de peso retenido multiplicando *100 y dividiendola sobre el peso total de la muestra, que se calcula con la funcion sum()
TablaGranulometrica['% Retenido Acumulado']=(peso_retenido*100/peso_retenido.sum()).cumsum() # La columna se calcula, tomando el valor obtenido de % Retenido y aplicando la funcion cumsum() que suma casilla a casilla y devuelve el valor en cada casilla   
TablaGranulometrica['% Pasa']=100-(peso_retenido*100/peso_retenido.sum()).cumsum()           # La columna se calcula tomando 100 y restando el % Retenido Acumulado  
TablaGranulometrica['Peso Pasa(gr)']=peso_retenido.sum()-peso_retenido.cumsum()              # La columna se calcula tomando el peso total que se calcula con la duncion sum() menos el peso retenido acumulado que se calculla con la funcion cumsum()  
print(TablaGranulometrica)

porcentaje_pasa=100-(peso_retenido*100/peso_retenido.sum()).cumsum()
TablaCoeficientes = pd.DataFrame({
    'Tamiz':tamiz,
    'Diametro (mm)':  diametro_tamiz,
    '% Pasa':porcentaje_pasa
})
TablaCoeficientes.drop(7, axis=0)
print(TablaCoeficientes)               #Se crea una tabla con los datos necesaios para determinar el D10,D30 y el D60, se elimina con la duncion drop la ultima fila de la tabla para que el programa no presente errrores 


