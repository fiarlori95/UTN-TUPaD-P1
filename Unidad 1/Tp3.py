#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
edad = int(input("ingrese una edad"))
if edad >= 18:
    print("Es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
#mensaje “Desaprobado”.
nota = int(input("ingrese una nota"))
if nota >= 6:
    print("aprobado")
else:
    print("desaprobado")

#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
#número par, imprimir por pantalla el mensaje "Ha ingresado un número par"; en caso
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
#operador de módulo (%) en Python para evaluar si un número es par o impar.
numero = int(input("ingrese un numero par"))

if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un número par")


#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
#siguientes categorías pertenece:
#● Niño/a: menor de 12 años.
#● Adolescente: mayor o igual que 12 años y menor que 18 años.
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
#● Adulto/a: mayor o igual que 30 años.

edad = int(input("ingrese una edad"))

if edad < 12:
    print ("Niño/a")
elif edad >= 12 and edad < 18:
    print ("Adolescente")
elif edad >= 18 and edad < 30:
    print ("Adulto/a joven")
else:
    print ("Adulto/a")

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
#como una lista o un string
contraseña= input("ingrese una contraseña entre 8 y 14 caracteres")

if len (contraseña) >=8 and len(contraseña)<=14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6) Escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

import random
from statistics import mode, median, mean

# Crear una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular moda, mediana y media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Imprimir los resultados
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Comparar y determinar el sesgo
if media > mediana > moda:
    print("Sesgo positivo (a la derecha)")
elif media < mediana < moda:
    print("Sesgo negativo (a la izquierda)")
else:
    print("Sin sesgo")

#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
#pantalla.
texto = input("escribe una palabra o frase")

vocales = "aeiouAEIOU"

if texto[-1] in vocales:
    texto += "!"
print(texto)

#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
#dependiendo de la opción que desee:
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
nombre = input("ingrese su nombre ")
numero = int(input("ingrese un numero 1 ,2 , o 3 "))
if numero == 1:
    nombre=nombre.upper()
    print(nombre)
elif numero == 2:
    nombre=nombre.lower()
    print(nombre)
elif numero == 3:
    nombre=nombre.title()
    print (nombre)
else:
    print("numero no valido, ingrese un numero 1, 2, o 3")

#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
#por pantalla:
#● Menor que 3: "Muy leve" (imperceptible).
#● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
#● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
#generalmente no causa daños).
#● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
#débiles).
#● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magnitud= int(input("ingrese una magnitud de terremoto"))

if magnitud < 3:
    print("Muy leve, imperceptible")
elif magnitud >= 3 and magnitud < 4:
    print("Leve, ligeramente perceptible")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado, sentido por personas pero generalmente no causa daños")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte, puede causar daños en estructuras débiles")
elif magnitud >=6 and magnitud < 7:
    print("Muy fuerte, puede causar daños significativos")
else:
    print ("Extremo, puede causar graves daños a gran escala")

#10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año
#Periodo del año                                Estación HN    Estación HS
#Desde el 21 de diciembre hasta el 20 de        INVIERNO        VERANO
#marzo (incluidos)
#Desde el 21 de marzo hasta el 20 de junio      PRIMAVERA       OTOÑO
#(incluidos)
#Desde el 21 de junio hasta el 20 de            VERANO          INVIERNO
#septiembre (incluidos)
#Desde el 21 de septiembre hasta el 20 de       PRIMAVERA       OTOÑO
#diciembre (incluidos)
#Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
#si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("ingrese en que hermisferio se encuentra norte o sur ").lower()
mes = input("ingrese en que mes del año se encuentra ").lower()
dia = int(input("ingrese en que dia se encuentra "))
if hemisferio== "norte":
    if (mes=="enero" or mes=="febrero"):
        print("Es invierno")
    elif (mes=="diciembre") and dia >= 21:
        print ("Es invierno")
    elif (mes== "marzo") and dia <= 20:
        print ("Es invierno")
    elif (mes == "abril" or mes == "mayo"):
        print ("Es primavera")
    elif (mes=="marzo") and dia >= 21:
        print("Es primavera")
    elif (mes=="junio") and dia <= 20:
        print("Es primavera")
    elif (mes== "julio" or mes == "agosto"):
        print ("Es verano")
    elif (mes=="junio") and dia >= 21:
        print ("Es verano")
    elif (mes=="septiembre") and dia <= 20:
        print("Es verano")
    elif (mes=="octubre" or mes=="noviembre"):
        print("Es otoño")
    elif(mes=="septiembre") and dia >= 21:
        print("Es otoño")
    elif (mes== "diciembre") and dia <= 20:
        print("Es otoño")
    else:
        print("Mes inválido")
elif hemisferio== "sur":
    if (mes=="enero" or mes=="febrero"):
        print("Es verano")
    elif (mes=="diciembre") and dia >= 21:
        print ("Es verano")
    elif (mes== "marzo") and dia <= 20:
        print ("Es verano")
    elif (mes == "abril" or mes == "mayo"):
        print ("Es otoño")
    elif (mes=="marzo") and dia >= 21:
        print("Es otoño")
    elif (mes=="junio") and dia <= 20:
        print("Es otoño")
    elif (mes== "julio" or mes == "agosto"):
        print ("Es invierno")
    elif (mes=="junio") and dia >= 21:
        print ("Es invierno")
    elif (mes=="septiembre") and dia <= 20:
        print("Es invierno")
    elif (mes=="octubre" or mes=="noviembre"):
        print("Es primavera")
    elif(mes=="septiembre") and dia >= 21:
        print("Es primavera")
    elif (mes== "diciembre") and dia <= 20:
        print("Es primavera")
    else:
        print("Mes inválido")
else:
    print("Hemisferio inválido")
    

           
    
