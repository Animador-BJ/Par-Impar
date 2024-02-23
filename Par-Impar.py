# Ejercicio N°4 Poder diferenciar si un numero es par o es impar

# input

print("-------------------------------------")
X = int(input("Digite el valor de x: "))


# Prosessing

r = X % 2
if r == 0:
    rta = " PAR"
    print("El Numero es Par")

else:
    rta = " IMPAR"
    print("El Numero es Impar")
print("-------------------------------------")
# output

print("-------------------------------------")
print("El numero " + str(X) + " es" + rta) 
print("-------------------------------------")