
+++++++++++++++++++
CURSO PYTHON
+++++++++++++++++++





**SESION 1 (17-agosto)

>ipython

>2+13 		#suma de enteros
>5/7  		#division de enteros
>5./7.		#division con decimales
>from __future__ import division #elimina la necesidad de poner punto decimal para indicar que son numeros fraccionados


-----------------------
Asignacion de variables:
-----------------------
>a=1.
>casa=1
>1a=1 		#caso NO VALIDO
>a1=1 		#caso VALIDO
>a1=1.		#entero con decimales
>a1=5e-3	#exponencial
>a1='cadena'	#nombre literal/cadena de texto

#al asignar una variable con un valor, lo estamos identificando como un OBJETO

>import numpy as np #importa la librería numpy que aligera asignación de variables a números
>np.pi		#da el valor de pi
>a1.real	#función de numpy que solo toma la parte real de un objeto (hay muchas funciones)


-----------
Comentarios
-----------

Con gato (comentario de UNA linea) #hola jejejejejejeje
Con tres comillas dobles (comentario indefinido, hasta cerrar las comillas) """hola jejejeje"""


----------------
Tipos de valores
----------------
			     símbolo		      ejemplo
-enteros 			i			5
-flotantes 			f			
-cadenas			s			'hola' "hola" 'este texto es una "broma"'
-complejos			c			1+3j
-boleanos			b			3<5 arroja True
							3>5 arroja False



ejemplo de complejos:
>a1=1+3j
>a1.real #arroja 1
>a1.imag #arroja 3

ejemplo de boleanos

a=3<5 	#python guarda el valor a=True
b=8>10	#python guarda el valor b=False
c=not b #python niega el valor de b, entonces c=True
if a is True:
	print 'correct'


---------------------
Impresion de valores
---------------------

>print 3	#python 2.7
>print (3)	#python 3.6
#puede ir CON o SIN espacio entre el "print" y el objeto

>print ("hola jeje")

>date=16
>print ("hoy es %i de agosto" %date)	#el i representa que date es un entero

>d=16
>m="agosto"
>a=2017

>print ("hoy es %i de %s de %i" %(d,m,a))	#caso 1
>print ("hoy es {} de {} de {}" .format(d,m,a))	#caso 2 (con función .format)

>pi=np.pi
>print ("pi={:.2f}" .format(pi))


----------------------
Propiedades de cadenas
----------------------

>a="cadena de texto" #los espacios indican que cada palabra es diferente, ie es una cadena de tres valores, hay un separador

>a.split()	#cuando la funcion está vacía (parentesis vacios), toma por default al espacio como separador:
	['cadena', 'de', 'texto']

>a.split("de")	#ahora toma como separador a "de"
	['ca', 'na ', ' texto']		#notar que ahora las palabras incluyen el espacio

>len(a)
	15

>a.upper()	#cambia las letras de mayusculas a minusculas
	'CADENA DE TEXTO'

>a.lower()	#al revés

Para ver cómo funciona cada función se puede dar:

>a.split?

y da información


------------
Contenedores
------------

	      signos
-Listas		[]
-Tuplas		()
-Diccionarios	{}

LISTAS

>L=[]
>len(L)
	0

>L=[3,5.4,'rojo']
>L+L
	[3, 5.4, 'rojo', 3, 5.4, 'rojo']
		#notar que la función de suma de lista no "suma" entrada con entrada, esto sucede porque la lista puede estar compuesta de varios tipos de objetos y no hay forma de sumar cadenas con cadenas rojo+rojo=?????

Para sumar entradas:

>L[0]
	3
>L[2]
	'rojo'
>L[-1]
	'rojo'
>L2=L+L		
		[3, 5.4, 'rojo', 3, 5.4, 'rojo'] #notar que hay 6 índices, es decir del 0 al 5
>L2[0:5]	#esta funcion imprime desde el indice 1 (o el 0 en notacion python) hasta el indice 4, es decir, imprime hasta el n-1 
>L2[0:6]	#esta funcion imprime todos los indices, pues ya no existe el indice 6, pero sí el 5

>L2[4]='verde'		#reemplaza el indice 4 por 'verde'
>L2.append('cafe')	#agrega esa cadena al final de la lista
>L2.insert(index,object)		#inserta al objeto ANTES del índice

ejemplo:

>L2.insert(1,5)
	[3, 5, 5.4, 'rojo', 3, 'verde', 'rojo', 'jiji']

TUPLAS 

las tuplas son como listas pero NO son modificables

>T=()
>T=('gato',5,2.3)
>T+T		#tiene la misma funcion que con listas

Para insertar elementos a la tupla, esto es INVALIDO:
>T[0]='perro'		#tuple object does not support item assignment
las tuplas no pueden ser modificadas


DICCIONARIOS

estan compuestos por cadenas
>A={'llave':valor}
>A={'gato':3}
>A.keys()
	'gato'

>A={'gato':[1,2,3], 'perro':'negro'}
>A.keys()
	['gato','perro']
>A.values()
	[[1,2,3], 'negro']
>A['gato']		#da el valor de la llave 'gato'
	[1,2,3]	
>A['gato']=[4,5,6]	#aqui estamos REDEFINIENDO el valor de la llave 'gato'
>A['gato']
	[4,5,6]
>A['gato'][1]		#da el valor de la primera entrada del valor de la llave 'gato'
	5
>A['gato'][1]=7		#aqui estamos REDEFINIENDO el valor de la primera entrada de la llave 'gato'

Recordar que esta modificacion de valores solo sirve para listas, no para tuplas




--------
Bloques
--------

-for
-if
-elif
-else
-while


Aqui vamos a ir llenando una lista vacía con un for:

>A=[]
>for i in [1,2,3]:
	x=i+1		#esta variable x solo es conocida dentro del for
	A.append(x)

>A
	[2,3,4]

> for i in [1,2,3]:
	x=i+1
        A.append(x)
          

>A
	[2, 3, 4]


>for i in [1,2,3]:
	if i<4:
	print('%i es menor que 4' %i)
                        
1 es menor que 4
2 es menor que 4
3 es menor que 4

>for i in [1,2,3]:
     ...:     if i<2:
     ...:         print('i es menor a 2')
     ...:     elif i==2:
     ...:         print('i es igual a 2')
     ...:     else:
     ...:         print('i es mayor a 2')
     ...:             
i es menor a 2
i es igual a 2
i es mayor a 2

>x=3
>while x<5:
	print('aun')
	x=x+1

aun
aun
aun


>range(5)
	[0,1,2,3,4]

>L=[3,4,5,6]
>len(L)
	4
>range(len(L))		#da las posiciones de las entradas de L
	[0,1,2,3]
	
>for i in range(len(L)):
	print (L[i]+1)
     
4
5
6
7

>L1=[3,4,5]
>L2=[1,2,3]
>for i1,i2 in zip(L1,L2):		#solo funciona si L1 y L2 tienen la misma longitud, i1 e i2 son los contadores que recorren a las listas L1 y L2 respectivamente, zip se usa para decirle al for que hay DOS listas o más

	print(i1+i2)

4
6
8

>for i in range(len(L1)):		#otra forma, más sencilla de hacer lo mismo que arriba, también las listas tienen que ser de la misma longitud

	print (L1[i]+L2[i])

4
6
8

>L3=[]
>L3=[i1+i2 for i1,i2 in zip(L1,L2)]

Para hacerlo con diccionarios:

>D={'valor_{}'.format(i):L1[i]+L2[i] for i in range(len(L1))}
>D
	{'valor_0': 4, 'valor_1': 6, 'valor_2': 8}



---------
Funciones
---------

-variables globales		#definidas en todo el código o dentro de un bloque, por ejemplo en un for
-variables locales		#definidas solo dentro de una función, para "sacarlas" es necesario un return

ejemplo:

>for i in range(5):
	y=i+2

>y
	6			#se guarda el último valor de y obtenido en el bloque for

-las funciones tienen argumentos:
	>def nombre_de_la_funcion(argumento1,argumento2,......,argumenton):
		funcionamiento

ejemplo:

>def suma(x1,x2):
	x=x1+x2
	return x

>suma(1,2)
	3

>suma(x1=1,x2=2)
	3

>suma(x2=2, x1=1)
	3

>def func(x,y,raiz=False)
	z=2
	if raiz is not False:
		z=5
	return x+y**z,z


--------------------------------------------------------------
--------------------------------------------------------------
Script base python
--------------------------------------------------------------
--------------------------------------------------------------

#!/usr/bin/env python
#-*- coding:utf-8 -*-

LIBRERIAS

UNIDADES

CUERPO DEL CODIGO

guardar como .py

--------------------------------------------------------------

para correr desde ipython:

>ipython
>cd /directorio/del/script
>% run script.py
>script(3,4,5)
>res=script(3,4,5)




