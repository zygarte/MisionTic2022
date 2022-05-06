def CDT(usuario: str, capital:int, tiempo: int):
    porcentaje_interes=0.03
    if (tiempo>2):
        valor_interes=(capital*porcentaje_interes*tiempo)/12
        valor_Total=capital+valor_interes
        return "Para el usuario "+ str(usuario) + " La cantidad de dinero a recibir, según el monto inicial "+ str(capital) +" para un tiempo de "+str(tiempo)+" meses es: "+str(valor_Total)
    else:
        porcentaje_interes=0.02
        valor_Perdida=(capital*porcentaje_interes)
        valor_Total=capital-valor_Perdida
        return "Para el usuario "+ str(usuario) + " La cantidad de dinero a recibir, según el monto inicial "+ str(capital) +" para un tiempo de "+str(tiempo)+" meses es: "+str(valor_Total)
##ejemplos
##print(CDT("AB1012",1000000,3))
##print(CDT("ER3366",650000,2))

print("Usuario")
usuario=input()
print("monto inicial")
capital=int(input())
print("tiempo")
tiempo=int(input())
print(CDT(usuario,capital,tiempo)) 