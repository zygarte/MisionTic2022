# Si el número es Palíndromo e impar, la presentacion corresponde a un chocolate amargo, y se retorna "BITTER".
# Si el número es Palíndromo y par, la presentacion corresponde a un chocolate dulce, y se retorna "SWEET". 
# Si el número es par, pero no palíndromo, la presentación corresponde a un chocolate con canela y clavos,
#  y se retorna "CINNAMON". Si el número es impar, pero no palíndromo,
#  la presentacion corresponde a un chocolate bajo en grasa, y se retorna "LIGHT"

def palidromo(numero:int)->bool:
    centena=numero//100
    decena=(numero-centena*100)//10
    unidad=numero-centena*100-decena*10

    if centena == unidad:
        resultado = True
    else:
        resultado = False
    return resultado

def espar(numero:int)->bool:
    if numero % 2 == 0:
        resultado = True
    else:
        resultado = False
    return resultado

def clasificar_chocolate(codigo:int)->str:
    if palidromo(codigo):
        if espar(codigo):
            resultado = "SWEET"
        else:
            resultado = "BITTER"
    else:
        if espar(codigo):
            resultado = "CINNAMON"
        else:
            resultado = "LIGHT"
    return resultado            

print(clasificar_chocolate(123))
print(clasificar_chocolate(222))   
print(clasificar_chocolate(111))
print(clasificar_chocolate(505)) 
print(clasificar_chocolate(576)) 