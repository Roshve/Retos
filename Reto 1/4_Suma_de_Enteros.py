# Reto #4 “Suma de enteros”
# Instrucciones: otro clásico conocido,
# donde pedirás al usuario que ingrese 2 números y
# muestre en pantalla el resultado.
# Si quieres añadir más dificultad puedes utilizar números con punto decimal y
# especificar el número de decimales después del punto.
# Ejemplo: 2.5633 + 5.6883 = 8.25

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
Suma = num1 + num2
print(num1, " + ", num2, " = ", "{0:.2f}".format(Suma))

#Recordarme del .format(var) va a estar dificil jejeje