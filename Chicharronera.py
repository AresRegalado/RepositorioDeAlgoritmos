import math

a = (int(input("Dame el valor de a:" )))
b = (int(input("Dame el valor de b:" )))
c = (int(input("Dame el valor de c:" )))
x1 = 0

par1=(b*b)
par2=(4*a*c)
x1 = (par1)-(par2)


if x1<0:
    temp1=x1*(-1)
       

if temp1>0 :
    raiz1=(math.sqrt(temp1))
    a = a * 2
    print("x1=(",'-',b,"+",raiz1,"i",")/",a)
    print("x2=(",'-',b,"-",raiz1,"i",")/",a)
else:
    raiz1=(((-1)*b)+math.sqrt(x1))/(2*a)
    raiz2=(((-1)*b)-math.sqrt(x1))/(2*a)
    print("x1=",raiz1)
    print("x2=",raiz2)