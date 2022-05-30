#! pip install pandas
#! conda install pandas

import pandas as pd

#ruta file csv
rutaFileCsv = 'https://github.com/luisguillermomolero/MisionTIC2022_2/blob/master/Modulo1_Python_MisionTIC2022_Main/Semana_5/Reto/movies.csv?raw=true' 

def listaPeliculas(rutaFileCsv: str)-> str:
    if rutaFileCsv.split(',')[-1] != 'csv': 
        try:
            #primer requisito, aplicar pd.read_csv()
            csv = pd.read_csv(rutaFileCsv)            

            #Se seleccionan las columnas 'Country','Language', 'Gross Earnings' para aplicar la fórmula de resumen
            subGrupoPeliculas = csv[[ 'Country','Language', 'Gross Earnings']]

                       #Segundo requisito, con pivot_table indexamos 'Country', 'Language'
            Coleccion = subGrupoPeliculas.pivot_table(index=['Country', 'Language'])
            #tercer requisito, solo 10 registros
            #print(Coleccion.head(10))
            # #Se importa la libreria matplotlib.pyplot
            # import matplotlib.pyplot as plt
            # Coleccion.plot()
            # #Se muestra la columna 'Net Earnings' [76 rows x 1 columns]
            # print('\n Ganancia por Año')
            # #Se muestra el resultado con la grafica
            # plt.show()
        except:  
            print(f'Error al leer el archivo de datos.')
    else:
        print(f'Extensión inválida.')
    return Coleccion.head(10)
    pass
print(listaPeliculas(rutaFileCsv))