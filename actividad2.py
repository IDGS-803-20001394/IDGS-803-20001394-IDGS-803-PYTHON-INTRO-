def sumar(x,y):
    suma="La suma de {} + {} es {}".format(x,y,(x+y))
    print(suma)

def restar(x,y):
    resta="La resta de {} - {} es {}".format(x,y,(x-y))
    print(resta)

def dividir(x,y):
    divison="La división de {} / {} es {}".format(x,y,(x/y))
    print(divison)

def multiplicar(x,y):
    suma="La multiplicación de {} * {} es {}".format(x,y,(x*y))
    print(suma)

def main():
    num1=int(input("Introduce el primer número: "))
    num2=int(input("Introduce el segundo número: "))
    opc=0
    while opc !=5:
        print("***********************************")
        print("1. Suma")
        print("2. Restar")
        print("3. Dividir")
        print("4. Multiplicar")
        print("5. Salir")
        opc=int(input("Selecciona una opción: "))

        if opc==1:
            sumar(num1,num2)
        elif opc==2:
            restar(num1,num2)
        elif opc==3:
            dividir(num1,num2)
        elif opc==4:
            multiplicar(num1,num2)
        elif opc==5:
            print("Adios...")
        else:
            print("Seleccione una opción valida")


if __name__=="__main__":
    main()

