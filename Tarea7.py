a=(int(input("numero 1\n")))
b=(int(input("numero 2\n")))
def add(a,b):
    if a==None or b==None:
        return 
    return a+b
print("Suma del numero 1 y 2\n") 
print(add(a,b),"\n")

def subtract(a,b):
    if a==None or b==None:
        print("pon un numero")
        return
    return a-b
print("Resta del numero 1 y 2\n")
print(subtract(a,b),"\n")

def multiply(a,b):
    if a==None or b==None:
        print("pon un numero")
        return
    return a*b
print("Multiplicacion del numero 1 y 2\n")
print(multiply(a,b),"\n")

def divide(a,b):
    if a==None or b==None:
        print("pon un numero")
        return
    return a/b
print("Divicion del numero 1 y 2\n")
print(divide(a,b),"\n")