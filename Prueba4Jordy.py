#Ejercicio sumar dos valores

#Algoritmo
#Dos variables que guarden la informacion de entrada.
#Una variable que guarden el resultado de la operación
#Comprobar si los valores introducidod por el usuario, son numero o no lo son.
    #Si son numeros, hacer la correspondiente operacion
    #Si no, escribir "parametros de entrada no validos"

import numbers

def operaciones(variable1,variable2):
    num1 = variable1
    num2 = variable2
    resultado = 0
    ListaResultados = [0,0,0,0,0]

    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):
        
        #Suma de dos valores (+)
        resultado = num1 + num2 

        #Resta de dos valores (-)
        resultado = num1 - num2 

        #Multiplicacion de dos valores (+)
        resultado = num1 * num2 

        #Division de dos valores (+)
        resultado = num1 / num2

        print(resu)

    else:
        print("ERROR")

operaciones(4,2)