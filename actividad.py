
num=int(input("Dame un numero: "))
lista=[1,2,3,4,5,6,8,9,10]

def multiplicar():
    for x in lista:
        print(str(num)+"x"+str(x)+"="+str(num*x))
        
multiplicar()