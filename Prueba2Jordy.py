def fib(xxx):
    a = 0
    b = 1

    while a < xxx:
        print(a,end='')
        a = b
        b = a + b
        print()
        b = "hola"

    print("fin del programa")
    
fib(10000)


def imprimir(texto):
    print(texto)
    
    
imprimir("Hola mundo cruel")
    #for (i;i<1000;i++)
    #do while 