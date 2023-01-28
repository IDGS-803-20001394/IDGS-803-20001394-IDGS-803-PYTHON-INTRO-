
class operacionesBasicas:
    x=0
    y=0

    def sumar(self):
        suma="La suma de {} + {} es {}".format(self.x,self.y,(self.x+self.y))
        print(suma)

    def restar(self):
        resta="La resta de {} - {} es {}".format(self.x,self.y,(self.x-self.y))
        print(resta)

    def dividir(self):
        divison="La división de {} / {} es {}".format(self.x,self.y,(self.x/self.y))
        print(divison)

    def multiplicar(self):
        suma="La multiplicación de {} * {} es {}".format(self.x,self.y,(self.x*self.y))
        print(suma)

def main():
    num1=int(input("Introduce el primer número: "))
    num2=int(input("Introduce el segundo número: "))
    obj = operacionesBasicas()
    obj.x=num1
    obj.y=num2
    opc=0
    while opc !=5:
        print("***********************************")
        print("1. Suma \n2. Resta \n3. División \n4. Multiplicación \n5. Salir")
        opc=int(input("Selecciona una opción: "))

        if opc==1:
            obj.sumar()
        elif opc==2:
            obj.restar()
        elif opc==3:
            obj.dividir()
        elif opc==4:
            obj.multiplicar()
        elif opc==5:
            print("Adios...")
        else:
            print("Seleccione una opción valida")

if __name__=="__main__":
    main()
