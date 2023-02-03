# Reto #5 “Suma y multiplicación”
# Instrucciones: añadiendo un extra al reto anterior ahora el usuario ingresará 3 números,
# sumarás los 2 primeros y el resultado será multiplicado por el tercero.
# Añade las consideraciones del punto decimal del reto anterior.
# Ejemplo:
# Datos de entrada:2, 3, 4
# Resultado:20

num1 = float(input("Ingresa primer numero: "))
num2 = float(input("Ingresa segundo numero: "))
num3 = float(input("Ingresa tercer numero: "))
suma = num1 + num2
multi = suma * num3
print("Datos de entrada: ", num1,", ", num2,", ", num3,"\nResultado: ", "{0:.2f}".format(multi))