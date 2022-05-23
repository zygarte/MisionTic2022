from functools import reduce as rd #Importar la funcion "reduce" desde la libreria "functools"

def ordenes(rutinaContable):
    
    
    
    #Para el desarrollo de esta implementación, el programador debe permitir introducir un
    #registro de ordenes desde una lista de tuplas y a través de la función “map”, “reduce” y “lambda”
   


    #Suma el incremento si la compra no llega a un mínima de 600.000 pesos
    

    #Lambda, Sumar el total de cada tupla de cada lista
    #Recorrido x, obtener numero de cada orden
    #Recorrido y, multiplica cantidad * precio
    factura = list(map(lambda x: [x[0]] + list(map(lambda y: y[1]*y[2], x[1:])), rutinaContable))
    


    #Lambda, Sumar los totales obtenidos de cada lista
    #Recorrido x, obtener numero de cada orden
    #Recorrido a, b , usa la funcion reduce para obtener un valor por lista, pero primero se suman los valores previos
    #y se procede con el redondeo a 2 decimales
    factura = list(map(lambda x: [x[0]] + [rd(lambda a,b: round(a + b,2), x[1:])], factura))
     
    #Lambda, verificar aumento de 25.000 pesos
    #Si el valor de la orden de cada lista es menor a ordenBase(600000), suma 25.000 pesos al total.
    ordenBase = 600000

    factura = list(map(lambda x: x if x[1] >= ordenBase else (x[0], x[1] + 25000), factura))
    
    print('------------------------ Inicio Registro diario ---------------------------------')
    #Ciclo para imprimir el total de cada compra
    for x in range(len(factura)):
        print(f'La factura {factura[x][0]} tiene un total en pesos de {factura[x][1]:,.2f}')
    print('-------------------------- Fin Registro diario ----------------------------------')

#Registro diario

rutinaContable = [ [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)], 
                   [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
                   [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
                   [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)] 
]
ordenes(rutinaContable)

rutinaContable = [ [6587, ("3268", 4, 25842.99), ("8274",18,23254.99), ("6548", 9, 48951.95), ("2547", 5, 8951.95)], 
                   [6588, ("1254", 3, 115362.58), ("9744", 2, 99235.66)],
]
ordenes(rutinaContable)

rutinaContable = [ [6589, ("9874", 1, 125698.20), ("88112", 2, 135645.20), ("3218", 4, 13645.20)],
                   [6590, ("5236", 8, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)],
                   [6591, ("7812", 2, 11.99), ("9652",11,18.99)],
]
ordenes(rutinaContable)

rutinaContable = [ [7172, ("1598", 6, 654.99), ("88112", 5, 390.95)],
                   [7173, ("3574", 8, 25689.99), ("521478",11,18.99), ("3215", 5, 390.95), ("88112", 5, 390.95)],
                   [7174, ("4896", 4, 12547.99), ("96321",11,18.99), ("5321", 5, 390.95), ("45621", 5, 390.95), ("65987", 5, 390.95)],
                   [7175, ("6254", 3, 8521.99), ("6548",11,18.99), ("88112", 5, 390.95)],
]
ordenes(rutinaContable)

rutinaContable = [ [7176, ("1296", 1, 9632.99), ("32187",11,18.99), ("88112", 5, 390.95), ("8274",18,23254.99)],
                   [7177, ("4589", 2, 147852.99), ("325698",11,18.99), ("88112", 5, 390.95)],
                   [7178, ("6798", 4, 78541.99), ("85214",11,18.99), ("325698", 5, 390.95)] 
]
ordenes(rutinaContable)