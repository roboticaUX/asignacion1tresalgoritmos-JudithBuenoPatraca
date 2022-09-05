print("ingrese un numero")
num = int(input())
fact = 1
for i in range(1, num+1): #el rango para el funcionamiento repetitivo
     fact*=i
print("El numero de",num, "es: ",fact)
