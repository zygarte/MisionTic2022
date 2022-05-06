def mostrar_mayor(v1,v2,v3):
    if v1>v2 and v1>v3:
        print("El valor mayor de los tres nuemros es: ",v1)
    else:
        if v2>v3:
            print("El valor mayor de los tres nuemros es: ",v2)
        else:
            print("El valor mayor de los tres nuemros es: " ,v3)

def cargar():
    v1=int(input("Ingrese el primer valor: "))
    v2=int(input("Ingrese el segundo valor: "))
    v3=int(input("Ingrese el tercer valor: "))
    mostrar_mayor(v1,v2,v3)

#programa principal
cargar()


