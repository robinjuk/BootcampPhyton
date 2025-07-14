import numbers

#Añado un nuevo parametro que indique el operador
def operaciones(variable1,variable2,variable3):
    num1 = variable1
    num2 = variable2
    operador = variable3
    ListaResultados = [0]
    nombreResultados = [0]

    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):
#Ahora como hago solo una operacion a la vez puedo quitar el numero de posicion de "Lista resultados"        
        if (operador == "+"):
            #Suma de dos valores (+)
            ListaResultados[0] = num1 + num2
            nombreResultados[0] = "Suma"
        
        elif (operador == "-"):
            #Resta de dos valores (-)
            ListaResultados[0] = num1 - num2
            nombreResultados[0] = "Resta" 
        
        elif (operador == "*"):
            #Multiplicacion de dos valores (*)
            ListaResultados[0] = num1 * num2 
            nombreResultados[0] = "Multiplicacion"

        elif (operador == "/"):
            #Division de dos valores (/)
            ListaResultados[0] = num1 / num2
            nombreResultados[0] = "Division"
        elif operador == "**":
            #Numero potenciado
            ListaResultados[0] = num1 ** num2
            nombreResultados[0] = "Potencia"
        
        
        else:
            print("Operador no válido")

        print(f"El resultado de la {nombreResultados[0]} es: {ListaResultados[0]}")
        
    else:
        print("ERROR")

operaciones(4,2,"+")