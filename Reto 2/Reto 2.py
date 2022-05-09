def cliente (informacion:dict)-> dict:
    id_cliente = informacion.get('id_cliente')
    nombre = informacion.get('nombre')
    edad = informacion.get('edad')
    primer_ingreso=informacion.get('primer_ingreso')
    atraccion="N/A"
    total_boleta="N/A"
    apto=True
    if(edad>18):
        atraccion="X-Treme"
        total_boleta="20000"
        if(primer_ingreso):
            total_boleta =(int(total_boleta))-(int(total_boleta)*0.05)
        else:
            total_boleta=int(total_boleta)
    elif(edad>=15 and edad<=18):
        atraccion="Carros chocones"
        total_boleta="5000"
        if(primer_ingreso):
            total_boleta =(int(total_boleta))-(int(total_boleta)*0.07)
        else:
            total_boleta=int(total_boleta)
    elif(edad>=7 and edad<15):
        atraccion="Sillas voladoras"
        total_boleta="10000"
        if(primer_ingreso):
            total_boleta =(int(total_boleta))-(int(total_boleta)*0.05)
        else:
            total_boleta=int(total_boleta)
    else:
        apto=False

    return {'nombre' : nombre, 'edad': edad, 'atraccion': atraccion, 'apto':apto, 'primer_ingreso':primer_ingreso, 'total_boleta':total_boleta}


    pass


# informacion = {
#     'id_cliente':0,
#     'nombre':"N/A",
#     'edad':0,
#     'primer_ingreso':False
#     }

informacion = {
    'id_cliente':1,
    'nombre':"Johana Fernandez",
    'edad': 20,
    'primer_ingreso':True
    }

print(cliente(informacion))

informacion = {
    'id_cliente':1,
    'nombre':"Johana Fernandez",
    'edad': 20,
    'primer_ingreso':False
    }
print(cliente(informacion))

informacion = {
    'id_cliente':2,
    'nombre':"Gloria Suarez ",
    'edad': 3,
    'primer_ingreso':True
    }
print(cliente(informacion))

informacion = {
    'id_cliente':3,
    'nombre':"Gloria Suarez ",
    'edad': 17,
    'primer_ingreso':True
    }
print(cliente(informacion))

informacion = {
    'id_cliente':3,
    'nombre':"Gloria Suarez ",
    'edad': 17,
    'primer_ingreso':False
    }
print(cliente(informacion))

informacion = {
    'id_cliente':3,
    'nombre':"Tatiana Ruiz ",
    'edad': 8,
    'primer_ingreso':True
    }
print(cliente(informacion))

informacion = {
    'id_cliente':3,
    'nombre':"Tatiana Ruiz ",
    'edad': 8,
    'primer_ingreso':False
    }
print(cliente(informacion))