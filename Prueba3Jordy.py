import numbers

def fib(numero):
    #Precondicion: El valor de entrada debe de ser un numero entero
    
    #Definicion de las variables a emplear
    a = 0
    b = 1

    #Se comprueba que el valor de entrada es un numero entero
    #si el valo r no es un numero, entonces se le dice al usuario quie el valor es incorrecto y que vuelva a probarlo
    #En caso de que no, pues se ejecueta el algoritmo
    if isinstance(numero, numbers.Number):
        print("es un numero")

        #Algoritmo
        while a < numero:
                print(a,end='')
                a = b
                b = a + b
                
                #Valores de salida
                print()

        print("fin del programa")              
    else:
        print("no es un numero")

fib(1000)
#Precondiciones
#El parametro qye va a recibir la funcion, debe de ser númerico

#postcondiciones