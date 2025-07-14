import numbers

def multiplo(variable1):

    numero = variable1

    if isinstance (numero, numbers.Number):
        resto = numero % 2

        if resto == 0:
            print(f"El número {numero} Es múltiplo de 2")
        else:
            print(f"El número {numero} no es múltiplo de 2")
        

    else:
        print("No has introducido un número válido")

multiplo(344)

#entrada = input("Introduce un valor: ")

#try:
#   numero_convertido = int(entrada)
#   multiplo(numero_convertido)
#except:
#    print("Eso no es un número válido.")
