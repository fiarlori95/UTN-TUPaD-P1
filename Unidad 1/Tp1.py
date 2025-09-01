#TODO EL TRABAJO REALIZADO

#1)crea un programa que imprima por pantalla el mensaje: “Hola Mundo!”
print("hola mundo")

# 2)Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#realizar la impresión por pantalla.
nombre= input("ingrese un nombre")
print (f"hola, {nombre}!")

#3)Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#“Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#la impresión por pantalla.
nombre = input ("ingrese su nombre")
apellido = input ("ingrese su apellido")
edad = int (input ("ingrese su edad"))
lugarResidencia = input ("ingrese su lugar de residencia")
print(f" Soy {nombre} {apellido} tengo {edad} y vivo en {lugarResidencia}")

# 4)Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.
radio= float (input("ingrese el radio de un circulo"))
area= 3.14 *(radio*radio)
perimetro= (2*3.14) * radio
print(f"el area del circulo es {area} y el perimetro del circulo es {perimetro}")

#5)Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#cuántas horas equivale
segundos= int (input("ingrese una cantidad de segundos"))
horas= segundos/3600
print (f"la cantidad de segundos ingresada equivale a {horas} horas")

#6)Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.
numero = int (input("ingrese un numero"))
print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)

#7)Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
numero1= int (input("ingrese un numero distinto de cero"))
numero2= int (input("ingrese un segundo numero distinto de cero"))
print(numero1+numero2)
print(numero1-numero2)
print(numero1*numero2)
print(numero1/numero2)

#8)Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#modo: IMC= peso/ altura*altura
altura= float (input("ingrese su altura"))
peso= float (input("ingrese su peso"))
imc= peso / (altura*altura)
print (f"el indice de masa corporal es {imc}")

#9)Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#TF=9/5*TC+32
temperaturaC= float(input("ingrese una temperatura en grados celsius"))
temperaturaF= 9/5*temperaturaC+32
print(f"la temperatura en grados celsius equivale a {temperaturaF}")

#10)Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#dichos números.
numero1 = int (input("ingrese un primer numero"))
numero2 = int (input("ingrese un segundo numero"))
numero3 = int (input("ingrese un tercer numero"))
promedio = (numero1+numero2+numero3) /3
print (f"el promedio es {promedio}") 

