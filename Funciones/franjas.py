from entradas import*
from funciones import*


'Instituto Nacional de Vías.Especificaciones Generales de Construcción de Carreteras.Art311.CAPÍTULO 3 ‐ AFIRMADOS, SUBBASES Y BASES'
afirmadoA38_limite_superior=[100,100,85,65,50,30,18]   #Franjas granulometricas para afirmado A-38(Tabla311-2 -Franjas granulométricas del material de afirmado)
afirmadoA38_limite_inferior=[80,75,60,40,30,13,9]

afirmadoA25_limite_superior=[100,100,90,70,55,35,20]   #Franjas granulometricas para afirmado A-25(Tabla311-2 -Franjas granulométricas del material de afirmado)
afirmadoA25_limite_inerior=[90,85,65,45,35,15,10]
  
SBG_50_limite_superior=[90,75,70,55,40,25,15]          #Franjas granulometricas para Sub Base Granular SBG-50 (Tabla320-3 - Franjas granulométricas del material de sub‐base granular)
SBG_50_limite_inferior=[60,45,40,25,15,6,2]

SBG_38_limite_superior=[90,85,75,60,45,30,15]          #Franjas granulometricas para Sub Base Granular SBG-38 (Tabla320-3 - Franjas granulométricas del material de sub‐base granular)
SBG_38_limite_inferior=[60,55,45,30,20,8,2]

BG_38_limite_superior=[90,85,75,60,45,30,15]           #Franjas granulometricas para Base Granular BG-38 de gradacion fina (Tabla 330 - 3. Franjas granulométricas del material de base granular)
BG_38_limite_inferior=[60,55,45,30,20,10,5]

BG_40_limite_superior=[90,75,68,50,32,20,9]            #Franjas granulometricas para Base Granular BG-40  de gradacion gruesa (Tabla 330 - 3. Franjas granulométricas del material de base granular)
BG_40_limite_inferior=[65,55,45,30,15,7,0]

tamices=[19,12,9.5,4.75,2,0.425,0.075]


plt.figure(figsize=(10,5))                              # Se asigna el tamaño a la grafica
plt.plot(TablaGranulometrica['Diametro (mm)'],TablaGranulometrica['% Pasa'], label='granulometria',color='black')   #Busca en la TablaGranulometria en la tabla los valores de diametro y el % pasa
plt.plot(tamices,afirmadoA38_limite_superior,color='blue',label='Lim Superior')           # Crea una curva granulometrica que indica que limite superior para catalogar el materia  
plt.plot(tamices,afirmadoA38_limite_inferior,color='red',label='Lim Inferior')            # Crea una curva granulometrica que indica que limite inferior para catalogar el materia 
plt.xscale("log")                                                                         # Asigna el tipo de escala de la grafica
plt.ylim([0, 100])
plt.gca().invert_xaxis()                                                                  # invierte el Eje x
plt.title('Curva Granulometrica Afirmado-A38', size=20)                                   # Se asigna el titulo General y los titulos de los ejes "x" y "y"
plt.xlabel("Diametro (mm)")
plt.ylabel("% Pasa")
plt.grid( color='green',linestyle='dotted', lw = 1)                                       # Se le indica que dibije la grilla en los dos sentidos. Se asigna un colo y un estilo de linea
plt.grid(True, which="minor", linestyle='dotted', color='green')
plt.legend()                                                                              # Crea una leyenda en la grafica 
plt.show()

  
plt.figure(figsize=(10,5)) 
plt.plot(TablaGranulometrica['Diametro (mm)'],TablaGranulometrica['% Pasa'], label='granulometria',color='black')
plt.plot(tamices,SBG_50_limite_superior,color='blue',label='Lim Superior')
plt.plot(tamices,SBG_50_limite_inferior,color='red',label='Lim Inferior')
plt.xscale("log")
plt.ylim([0, 100])
plt.gca().invert_xaxis()
plt.title('Curva Granulometrica SBG-50', size=20)
plt.xlabel("Diametro (mm)")
plt.ylabel("% Pasa")
plt.grid( color='green',linestyle='dotted', lw = 1)
plt.grid(True, which="minor", linestyle='dotted', color='green')
plt.legend()
plt.show()


plt.figure(figsize=(10,5)) 
plt.plot(TablaGranulometrica['Diametro (mm)'],TablaGranulometrica['% Pasa'], label='granulometria',color='black')
plt.plot(tamices,BG_40_limite_superior,color='blue',label='Lim Superior')
plt.plot(tamices,BG_40_limite_inferior,color='red',label='Lim Inferior')
plt.xscale("log")
plt.ylim([0, 100])
plt.gca().invert_xaxis()
plt.title('Curva Granulometrica BG-40', size=20)
plt.xlabel("Diametro (mm)")
plt.ylabel("% Pasa")
plt.grid( color='green',linestyle='dotted', lw = 1)
plt.grid(True, which="minor", linestyle='dotted', color='green')
plt.legend()
plt.show()

 