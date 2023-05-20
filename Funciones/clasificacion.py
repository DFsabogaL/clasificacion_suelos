from funciones import*

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