import numbers

#Añado un nuevo parametro que indique el operador
def operaciones():
    operador = input('Elija la operación a realizar: "+", "-",  "*", "/", "**": ')
    num1 = float(input("Primer número:"))
    num2 = float(input("Segundo número:"))
    ListaResultados = [0]
    nombreResultados = [0]

    if isinstance(num1, numbers.Number) and isinstance(num2, numbers.Number):
#Ahora como hago solo una operacion a la vez puedo quitar el numero de posicion de "Lista resultados"        
        match operador:
            case "+":
            #Suma de dos valores (+)
                ListaResultados[0] = float(num1 + num2)
                nombre = "suma"

            case "-":
                #Suma de dos valores (+)
                ListaResultados[0] = float(num1 - num2)
                nombre = "resta"

            case "*":
                #Suma de dos valores (+)
                ListaResultados[0] = float(num1 * num2)
                nombre = "multiplicación"

            case "/":
                #Suma de dos valores (+)
                ListaResultados[0] = float(num1 / num2)
                nombre = "división"

            case "**":
                #Suma de dos valores (+)
                ListaResultados[0] = float(num1 ** num2)
                nombre = "potencia"
        
        for i in range (len(ListaResultados)):
            print(f"El resultado de la {nombre} es:")
            print(ListaResultados[i])

        
    else:
        print("ERROR")

operaciones()