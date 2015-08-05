# -*- coding: utf-8 -*-         #ASÍ SE ADMITEN LOS CARACTERES ESPECIALES
__author__ = 'Alvaro'
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

a="¡Hola, mundo!"

for i in range(0,5,1):
    print(a+" Iteración: "+i.__str__())

print ("Esto es una prueba para gitHub")

#Formato de cadenas

cadena1 = "hola esto es una cadena"

cadena2 = "hola esto es \"" \
         "una cadena con salto"

#Bucle equivalente a for(int i = 0;i<10;i++)
a=0
for i in range(10):
    a+=i

print("Valor de la variable a tras finalizar el bucle: "+a.__str__())

#Tuplas:
a=(0,0)

print("Valor de la tupla a: "+a.__str__())


print("Valor de la tupla a: "+a.__str__())

#Esto es un generador:
cuadrados = (i**2 for i in range(10))

#Así se acceden a los valores del generador:
print(cuadrados.__next__())
print(cuadrados.__next__())
print(cuadrados.__next__())

print("*** Generador recorrido con un for ***")
cuadrados = (2**i for i in range(10))
for x in cuadrados:
    print(x)

#Listas
#Así se define una lista:
lista = [0,1,2,4,8,16,32,64]
print("Accediento a una posición de la lista: "+lista[0].__str__())
print("Accediento a una posición de la lista: "+lista[3].__str__())
print("Accediento a la lista a partir de la posición 4 "+lista[4:].__str__())
lista[0]=999
print("Accediento tras variar un valor: "+lista[0].__str__())

listaMixta=[4,654,"cadena",4.5]
print("Lista mixta: "+listaMixta.__str__())

lista2 = list([1,2,3,4,5])
print("Lista 2: "+lista2.__str__())

#Conjuntos
conjunto = {0,1,2,4,8,16,32,64}
print("Conjunto: "+conjunto.__str__())
conjunto2 = {1,2,32}

#Intersección
conjuntoRes = conjunto.intersection(conjunto2)
print("Conjunto intersección: "+conjuntoRes.__str__()+" Conj: "+conjunto.__str__()+" Conj2: "+conjunto2.__str__())

#Otra manera de declararlos
conjunto3 = set([1,2,3,8,45,156])
print("Conjunto3: "+conjunto3.__str__())

#Diccionario
diccionario = {"clave1": "valor1", "numero":5}
print("Diccionario: "+diccionario.__str__())
print("Consultando una clave del diccionario: "+diccionario.get("clave1"))
print("Si una clave no existe puedo darle un valor por defecto: "+diccionario.get("adasdas","No existe"))
#Así se añade un par clave/valor
diccionario["clave nueva"]="valor nuevo"
print("Tamaño del diccionario: "+diccionario.__len__().__str__())

#Forma fácil de definir un diccionario con string:
diccionario_string = dict(hola=0,adios=2,cuatricientos=400)

#Consultar el tipo de un objeto
print("Tipo de conjunto3: "+type(conjunto3).__str__(type(conjunto3)))

#Las arroba (@) son decoradores:
#@decorador

#Para operar sobre el objeto, pongo el valor entre paréntesis:
a=(1).__neg__().__str__()
print(a)

#Duplicar cadenas:
cadena = "abc"
cadena *=2
print(cadena)

#Cuando una función no sabe qué hacer, devuelve NotImplemented

#En python se pueden añadir funciones / propiedades privadas, pero el programador puede acceder a ellas desde
#cualquier sitio en cualquier momento. Una variable / función privada lleva el carácter "_" o "__" como prefijo
#de su nombre

#Las funciones con barra baja al principio y al final del nombre son funciones especiales a las que Python llama
#automáticamente bajo algunas circunstancias.

#Se puede acceder a un método privado usando: _+nombreclase+nombre del método privado. Ejemplo:
#objeto._MiClase__metodo_privado()



