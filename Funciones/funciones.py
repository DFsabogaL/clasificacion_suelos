from entradas import*

for i in range(0,len(TablaCoeficientes)):                         # Se crean 3 ciclos For, lo que hacen es recorrer las columnas de la TablaCoeficientes 
  if TablaCoeficientes.loc[i,'% Pasa']<=10 and TablaCoeficientes.loc[i-1,'% Pasa']>=10:     
                                                                  # Busca la condicion en que el porcentaje pasa es menor o igual a 10%(30 y 60 ) y establece que el dato inmediatamente anterior tiene que ser mayor o igual a 10%(30 y 60)
    D10_2porcentaje_pasa=TablaCoeficientes.loc[i,'% Pasa']        # Cuando incuentra la condicion dada en la TablaCoeficientes establece los valores semilla para calcular el D10,D30 y D60 
    D10_1porcentaje_pasa=TablaCoeficientes.loc[i-1,'% Pasa']    
    D10_1diametro=TablaCoeficientes.loc[i-1,'Diametro (mm)']
    D10_2diametro=TablaCoeficientes.loc[i,"Diametro (mm)"]
     


for j in range(0,len(TablaCoeficientes)):
  if TablaCoeficientes.loc[j,'% Pasa']<=30 and TablaCoeficientes.loc[j-1,'% Pasa']>=30: 
  
    D30_2diametro=TablaCoeficientes.loc[j,'Diametro (mm)']        # Ciclo para calcula D30
    D30_1diametro=TablaCoeficientes.loc[j-1,'Diametro (mm)']
    D30_2porcentaje_pasa=TablaCoeficientes.loc[j,'% Pasa']    
    D30_1porcentaje_pasa=TablaCoeficientes.loc[j-1,'% Pasa']


for k in range(0,len(TablaCoeficientes)):
  if TablaCoeficientes.loc[k,'% Pasa']<=60 and TablaCoeficientes.loc[k-1,'% Pasa']>=60:
       

    D60_2diametro=TablaCoeficientes.loc[k,'Diametro (mm)']         # Ciclo for para calcular D60
    D60_1diametro=TablaCoeficientes.loc[k-1,'Diametro (mm)']
    D60_2porcentaje_pasa=TablaCoeficientes.loc[k,'% Pasa']
    D60_1porcentaje_pasa=TablaCoeficientes.loc[k-1,'% Pasa']

print(D10_1diametro,D10_2diametro)

def coeficientes():                                                 # la funcion permite calcular el coeficiente de uniformidad y de curvatura
                                                                    # El calculo de D10, D30 y D60 se hace apartir de la ecuacion logaritmica para calcular el diametro correspondiente que deja pasar cada porcentaje 
  D10=((((D10_2diametro-D10_1diametro)/(math.log10(D10_2porcentaje_pasa)-math.log10(D10_1porcentaje_pasa)))*math.log10(10))-math.log10(D10_1porcentaje_pasa))+D10_1diametro 
  D30=((((D30_2diametro-D30_1diametro)/(math.log10(D30_2porcentaje_pasa)-math.log10(D30_1porcentaje_pasa)))*math.log10(30))-math.log10(D30_1porcentaje_pasa))+D30_1diametro
  D60=((((D60_2diametro-D60_1diametro)/(math.log10(D60_2porcentaje_pasa)-math.log10(D60_1porcentaje_pasa)))*math.log10(60))-math.log10(D60_1porcentaje_pasa))+D60_1diametro

  global coeficiente_uniformidad                                     # Se usa a funcion global para citar la varible global y modificarla de forma local 
  coeficiente_uniformidad=D60/D10
  global coeficiente_cuervatura
  coeficiente_cuervatura=D30*D30/D10*D60
  print(D10,D30,D60)
  return

def limites():                                                      # La funcion permite calcular el indice de plasticidad y captura la informacion del usuario del limite liquido y limite plastico
  global limite_liquido
  limite_liquido=float(input("Ingrese el Limite Liquido"))
  global limite_plastico
  limite_plastico=float(input("Ingrese el limite Plastico"))
  global indice_plasticidad
  indice_plasticidad=limite_liquido-limite_plastico
  print(f'El indice de plasticidad es {indice_plasticidad}')       # Nos arroja el valor de entrada para la grafica de suelos
  return

diametro200=float(0.075)                                           # Se establecen como constantes el diametro de los tamices No.4 y No. 200 con el onjetivo de poder operarlos mas abajo
diametroNo4=float(4.75)

def finos():                                                       # La funcion permite establecer la cantidad de material fino en un suelo granular grueso 
  finos_variable=TablaGranulometrica[TablaGranulometrica["Diametro (mm)"]==diametro200 ]['% Pasa']
  finos_variable2=float(finos_variable)                            # Es establece la variable finos_variable que busca en la TablaGranulometrica, en la columna de diametros el valor igual al diametro No.200 y asigna el valor del porcentaje pasa 
  
  if finos_variable2<5:                                            # La variable finos_variable2 toma la variable finos_variable y la convierte en un valor float para poder operar
    coeficientes()                                                 # Es establece unos condicionales para determinar las opeeraciones para el calculo de material fino 
  elif finos_variable2<12 and finos>5:
    coeficientes()
    limites()
  else:
    limites()
    return 

granulometria=TablaGranulometrica[TablaGranulometrica["Diametro (mm)"]==diametro200 ]["% Pasa"] 
granulometria2=float(granulometria)                                 # Se establece una variable llamada granulometria, busca el valor en la TablaGranulometrica de Diametro y asigna el % Pasa
if granulometria2<=50:                                              # La varible granulometria se reporta como un valor indexado que no se puede operar, por eso se crea la variable granulometria2 que tranforma el dato en un numero con la funcion float()
    print("El suelo esta conformado por su mayoria de material Grueso")         # Con el primer condicional se establece si el suelo es grueso o fino
    grava_arena=TablaGranulometrica[TablaGranulometrica["Diametro (mm)"]==diametroNo4 ]["% Pasa"]
    grava_arena2=float(grava_arena)                                 # Igual que en la variable granulometria, se busca el valor en la tabal y se trnsforma con la funcion float() 
   
    if grava_arena2>50:                                             # Se establece el tipo de suelo con un condicional, para seber si corresponde a arena o a grava 
      print("El suelo corresponde a una arena (S) ")
      finos()                                                       # Llamamos la funcion de finos para establcer las cualidades del tipo de suelo fino que corresponde a la muestra
      if coeficiente_uniformidad!=0 and limite_liquido!=0:          # Al estar establecidad las variables globales, se establece un condicional que verifique exclusivamente las variable modificadas por la funciones  
        if coeficiente_uniformidad>6 and 1<=coeficiente_cuervatura<=3:
          if indice_plasticidad<0.79*(limite_liquido-20) or indice_plasticidad<4:  # Codicional multiple para que busque la ubicacion en la grafica de suelos
            print("El suelo es una arena graduada con particulas de limo(SW-SM)")  # En la siguiente parte del codigo se establecen condicionales para que clasifique el suelo. 
          else:
            print("El suelo es una arena graduada con particulas de arcilla(SW-SC")# Se hace uso de condicionales com el if, elif y else para determinar la clasificacion del suelo
        else:
          if indice_plasticidad<0.79*(limite_liquido-20) or indice_plasticidad<4:
            print("El suelo es una arena pobremente graduada con particulas de limo (SP-SM)")
          else:
            print("El suelo es una arena pobremente graduada con particulas de arcilla(SP-SC)")
      elif coeficiente_uniformidad!=0:
        if coeficiente_uniformidad>6 and 1<=coeficiente_cuervatura<=3:
          print("El suelo es un arena gruesa(SW)")
        else:
          print("El suelo es un arena pobremente graduada(SP)")
      elif limite_liquido!=0:
        if indice_plasticidad<0.79*(limite_liquido-20) or indice_plasticidad<4:
          print("El suelo es una arena limosa (SM)")
        else:
          print("El suelo es una arena arcillosa(SC)")
    else:
      print("El suelo corresponde a una grava (G)")
      finos()
      if coeficiente_uniformidad!=0 and limite_liquido!=0:
        if coeficiente_uniformidad>4 and 1<=coeficiente_cuervatura<=3:
          if indice_plasticidad<0.79*(limite_liquido-20) or indice_plasticidad<4:
            print("El suelo es una grava graduada con particulas de limo(GW-GM)")
          else:
            print("El suelo es una grava graduada con particulas de arcilla(GW-GC") 
        else:
          if indice_plasticidad<0.79*(limite_liquido-20) or indice_plasticidad<4:
            print("El suelo es una grava pobremente graduada con particulas de limo (GP-GM)")
          else:
            print("El suelo es una grava pobremente graduada con particulas de arcilla(GP-GC)")
      elif coeficiente_uniformidad!=0:
        if coeficiente_uniformidad>6 and 1<=coeficiente_cuervatura<=3:
          print("El suelo es un grava graduada(GW)")
        else:
          print("El suelo es un grava pobremente graduada(GP)")
      elif limite_liquido!=0:
        if indice_plasticidad<0.79*(limite_liquido-20) or indice_plasticidad<4:
          print("El suelo es una grava limosa (GM)")
        else:
          print("El suelo es una grava arcillosa(GC)")
        
    
    


else:
  print("El suelo esta conformado por material fino")
  limites()
  if limite_liquido>50:
    if indice_plasticidad<0.79*(limite_liquido-20):
      print("El suelo es un Limo de Alta Plasticidad(MH)")
    else:
      print("El suelo es una arcilla de Alta Plasticidad (CH)")

  else:
    if indice_plasticidad<4 or indice_plasticidad<0.79*(limite_liquido-20):
      print("El suelo es un limo de baja plasticidad (ML)")
    elif indice_plasticidad<7 and indice_plasticidad>4 and indice_plasticidad>0.79*(limite_liquido-20):
      print("El suelo es un limo o arcilla de baja plasticidad (ML-CL)")
    else: 
      print("El suelo es una arcilla de baja plasticidad (CL)")