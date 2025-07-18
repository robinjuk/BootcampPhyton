def contador():
    for i in range (1, 101):
        print(i)
contador()

def imprimirnumeros_bis(limite):
    for i in range(1, limite):
        print("El numero actual es...")
        print(i)

imprimirnumeros_bis(100)

def imprimirnumeros():
    for i in range (1, 100):

        if  i & 2 == 0:
            print ("el numero es par y es el siguiente...")
            print(i)

imprimirnumeros()

    
