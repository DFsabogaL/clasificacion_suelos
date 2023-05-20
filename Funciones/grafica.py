from funciones import*
from entradas import*



ejex=np.arange(0,100,1)                # Se establece el eje x con un vector de 0 a 100 y de paso 1
linea1=np.arange(25.3,100,1)           # Se crea un vector que parte de 25.3 a 100, el dato 25.3 es el punto donde va a partir la linea A 
LineaU=np.arange(0,100)                # La linea U va a ser igual al vector x, con el fin de graficarla mas adelante a 45°
LineaA=0.75*(linea1-20)                # El primer componente de la linea A se establece con la inclinacion que debe tener que es de 0.75  
  
lineas50_1=[50,50]                     # Se establecen dos puntos para graficar la linea de 50% de limite liquido que divide la grafica en la mita
lineas50_2=[0,100]
  
lineax_CM1=[4,25.3]                    # Se establecen los 4 puntos para graficar las dos lineas que agrupan los suelos (CL-ML)
lineax_CM2=[7,29.3]
lineay_CM1=[4,4]
lineay_CM2=[7,7]

plt.figure(figsize=(20,10))            # Se asigna el tamaño de la grafica, para que sea claro

plt.plot(ejex,LineaU,color="red")      # Se crea la linea U, asignando como componente "y" el vector "LineaU" 
plt.plot(linea1,LineaA,color="blue")   # Se crea la Linea A, asignando como punto de partida el vector Linea1 y en componente "y" el vector LineaA, lo que hace que se obtenga la pendiente correspondiente
plt.plot(lineas50_1,lineas50_2,color="c",linestyle='dashed') # La linea se crea apartir de dos puntos
plt.plot(lineax_CM1,lineay_CM1,color="black")                # La linea se crea apartir de dos puntos
plt.plot(lineax_CM2,lineay_CM2,color="black")                # La linea se crea apartir de dos puntos
  
plt.grid()                                                   # Pone grilla en la grafica 
plt.title("Grafica de Plasticidad",size=25)                  # Pone titulo en la grafica
plt.xlabel("Limite Líquido LL (%)",size=18)                  # Pone titulo al eje "x"                
plt.ylabel("Indice de Plasticidad IP (%)",size=18)           # Pone titulo al eje "y" 

plt.plot(limite_liquido,indice_plasticidad, marker='X')              # Grafica en forma de x un punto con coordenadas(abscisa=limite liquido y ordenada=Indice de plasticidad)
plt.axvline(x=limite_liquido,color="black",linestyle='dotted')       # Grafica una linea vertical, su ubicacion esta determinada por el limite liquido, el estilo de linea es punteado 
plt.axhline(y=indice_plasticidad,color="black",linestyle='dotted')   # Grafica una linea horizontal, su ubicacion esta determinada por el indice de plasticidad, el estilo de linea es punteado  

plt.text(5,indice_plasticidad+1,f'IP={indice_plasticidad}',size=10,color="black")    # Se grafica un texto. Con la funcion f''me permite llamar una variable usando {} e indicar el indice de plasticidad  
plt.text(95,indice_plasticidad+1,f'IP={indice_plasticidad}',size=10,color="black")   # La ubicacion. se asigna una abscisa constante y la ordenada va a estar dada por el valor del Indice de Plasticidad +1 para que no este pegada a linea anteriormente creada 
plt.text(limite_liquido+1,2,f'LL={limite_liquido}',size=10,color="black")            # Se grafica un texto. Con la funcion f''me permite llamar una variable usando {} e indicar el Limite liquido 
plt.text(limite_liquido+1,68,f'LL={limite_liquido}',size=10,color="black")           # La ubicacion. se asigna una ordenada constante y la abscisa va a estar dada por el valor del Limite Liquido +1 para que no este pegada a linea anteriormente creada
  
plt.text(80,60,"(CH)",color="black",size=15)                 # Se grafica un texto. La ubicacion es por coordenadas definidas segun la ubicacion que deseamos sobre la grafica
plt.text(80,20,"(MH)",color="black",size=15)                 # Los textos corresponden a cada tipo de material
plt.text(35,25,"(CL)",color="black",size=15)                 # Se adigna un color y un tamaño al tecto
plt.text(35,2,"(ML)" ,color="black",size=15)
plt.text(15,5,"(CL-ML)",color="black",size=10)
plt.ylim(0,70)                                               # Se establecen lis limites de la grafica 
plt.xlim(0,100)
plt.show()                                                   # Se Grafica :D 