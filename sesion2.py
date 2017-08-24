
+++++++++++++++++++
CURSO PYTHON
+++++++++++++++++++


#NOTAAAAA: para saber cómo funciona alguna función se da (e.g) np.arange? (con signo de interrogación)



def fact(n):
	if n<=o:
		return 1
	return n*fact(n-1)

#1+2+3+.....+n=n(n+1)/2

def suma(n):
	if n<=0:
		print 'introduzca un número natural'
	return n*(n+1)/2

#ahora la forma recursiva:

def suma2(n):
	if n-1<0:
		print 'introduzca un número natural'
	if n == 1:
		return 1
	return n+suma(n-1) 

#Funciones LAMBDA
#estan hechas para funciones cortas (e.g. no necesitan identación, una sola línea, etc)

F=lambda x: (x-1)**2
F(2)	#=1
F(50)	#=2401
G=lambda x,y,z: (x**2+y**2+z**2)**0.5
G(1,2,3) #=no lo hice, pero sí sale jejeje
G(x=1,z=2,y=1)

#Importar librerías

from math import pi		#importar un solo elemento de la librería ocupa menos memoria que importar
from math import pi as p1	#a la librería completa
import math
import numpy as np		#para facilitar el uso
math.pi		#jala a pi en la misma línea
from math import *		#esto importa todas las funciones, pero NO ES RECOMENDABLE porque importa las 
				#funciones con su nombre original (e.g. sin, cos, pi) y no como math.sin, math.pi
#suponer que redefinimos math.pi
math.pi=4
#para resetear a configuracion inicial se utiliza:
reload (math)			#python 2
from importlib import reload	#python 3
reload (math)			#python 3

math.pi	#ya arroja el valor original

#Importar scripts

#ejemplo, si tenemos un script en nuestro directorio base llamado tarea.py el cual define funciones f1,f2,F,dict
#y queremos jalar estas funciones, utilizamos:

%run tarea.py			#equivalente a from tarea import *
import tarea			#equivalente a importar una librería
tarea.f1			#utiliza la función f1 de la "librería" tarea
from tarea import f1 as force

#Numpy

import numpy as np

l=[1,2,3,4,5,6]
a=np.array([1,2,3,4,5,6])	#un array necesita SOLO un parámetro para definirse, por ejemplo aquí: una lista
				#dada por [,,,,,]
a=np.array(1,2,3,4,5,6)		#ERROR, porque aquí hay 6 elementos
b=np.array((1,2,3))
c=np.array(l)			#para convertir a la lista l en un array
l2=[1,2,'perro']		#una lista definida con enteros y cadenas
d=np.array(l2)			
	#d=(['1','2','perro'])	i.e. el np.array convierte a los elementos en cadenas pues los enteros pueden
				#convertirse en cadenas (al agregar comillas) pero las cadenas nunca en enteros

a=np.array([1,2,3,4])			#vector
b=np.array([[1,2],[3,4]])		#matriz
c=np.array([[[1],[2]],[[3],[4]]])	#arreglo de matrices

c.shape		#nos da la forma del array, (4):vector de 4 entradas, (2,2): matriz de 2x2, (2,2,1): tensor de 2x2x1
b[0]		#nos da la primer entrada del array
b[0][1]		#segunda entrada de la primera entrada del array, es equivalente a:
b[0,1]		#equivalente al de arriba


#formando arrays:
#1:

l=range(5)
l2=np.array(l)

#2:

np.arange(0,5,1)	#np.arange(valor_inicial,valor_final,longitud_del_paso)
	#=array([0, 1, 2, 3, 4])
np.arange(0,5,2)
	#=array([0,2,4]),notemos que no incluyeel extremo derecho, esto es porque arange es de intervalo abierto por la derecha y cerrado por la izquierda

np.linspace(10,10000,100)	#np.linspace(valor_inicial,valor_final,numero_de_puntos), linspace es cerrado por la izquierda y por la derecha

np.linspace(10,10000,100,endpoint=False)	#no incluye el punto final

np.logspace(1,3,100)		#np.logspace(valor_inicial,elevado_a_la_potencia, numero_de_puntos)

np.zeros(2)			#entre paréntesis va el número de ceros que queremos
np.zeros([2,3]) o np.zeros((2,3)) #da una matriz de 2x3 de puros ceritows
np.zeros_like(l2)		#hace un arreglo con la misma forma que l2 pero con puros ceritows
np.ones_like(b)			#da same
np.ones_like(b)+6		#le suma 6 a cada uno
np.ones_like(b)/2		#divide a todo entre 2
np.pones_like(b, dtype=float)	#lo mismo pero convierte a las entradas en flotantes

#Memoria de arrays

a=np.array([1,2,4])
b=a
b[2]=5
print a	#=[1,2,5], significa que aunque queramos copiar al array a en b, si modificamos b, también modificaremos a a
#la manera correcta de copiar arrays es:

c=a.copy()	#de esta manera, al modificar c no se modifica a a


#Máscaras

a=np.arange(10,51,1)
a>15 	#arroja un arreglo de boleanos (true, false, etc) que indican qué valor del array es mayor que 15
	#array([False, False, False, False, False, False,  True,  True,  True,
        #True,  True,  True,  True,  True,  True,  True,  True,  True,
        #True,  True,  True,  True,  True,  True,  True,  True,  True,
        #True,  True,  True,  True,  True,  True,  True,  True,  True,
        #True,  True,  True,  True,  True], dtype=bool)
#para mas bien obtener un arreglo con TODOS los numeros (no en boleano) que cumplen esa condicion:

mask=a>15
a[mask]		#esto ya arroja el array:
	#array([16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32,
       #33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49,
       #50])

#para los valores 25<=1>40:

mask2=(a>=25)&(a<40)
a[mask2] #arroja del 25 al 40
a[~mask2]#arroja el recíproco de mask2, ie del 10 al 24 y del 40 al 50

#suponer que queremos saber qué valores IMAGEN de un array cumplen con la máscara
b=a**2	#de esta manera, b ya es DEPENDIENTE de a, es por así decirlo, una imagen del dominio (a)
#ahora aplicamos la máscara:
b[mask]
	#array([ 625,  676,  729,  784,  841,  900,  961, 1024, 1089, 1156, 1225,
       #1296, 1369, 1444, 1521])
#estos son los valores correspondientes a 16, 17, .......48,49,50 en el array a, i.e. aquellos que cumplen 
#con la condición de "mask"

#Cortar arrays

a=np.arange(10)

#nos interesa decirle qué indices queremos

a[1:8:3]	#a[indice_inicial:indice_final_abierto:paso] notar que el paso siempre debe ser un num entero
a[:4]		#toma todos los valores desde el inicio hasta el indice 4
a[2:]		#toma todos los valores despues del indice 2
a[::-1]		#toma todos los valores pero los invierte (i.e. los pasos negativos sí son válidos)
a[4:]=500	#esto redefine los valores mayores o iguales al 4to indice con un nuevo valor: 500

#CLASES

#una clase es algo así como una función pero más general, está arriba de la función en la jerarquía de python
#es recomendable que las clases estén escritas en mayúsculas

class GRAV(object):

	def __init__(self,m1,m2,R,G=6.67e-11):	#define a los parámetros m1,m2,etc en todos lados
		self.m1=m1
		self.m2=m2
		self.R=R
		self.G=G

	def fuerza(self):
		return self.G*self.m1*self.m2/(self.R**2)

	#sabemos que F también es igual a F=m1*(v1**2)/R, despejamos v1:
	
	def vel(self,calc_v1=False,calc_v2=False):
		if calc_v1 is True:
			m=self.m1
		elif calc_v2 is True:
			m=self.m2
		else:
			print ('error: no has seleccionado que masa quieres')

	
		return ((self.fuerza()*self.R)/m)**0.5 #self.fuerza calcula la fuerza con los parametros m1 y m2 originales (como arriba)

	def dict(self):
		D['fuerza']=self.fuerza()
		D['vel1']=self.vel(calc_v1=True)
		D['vel2']=self.vel(calc_v2=True)

#AHORA SI LO CORREMOS:

obj=GRAV(R=1,m1=3,m2=2)

obj.vel(calc_v1=True)


#las clases son utiles pues no debemos cargar todas las constantes desde el inicio del código (y estarlas arrastrando)
#sino que se pueden definir las constantes SOLO dentro del __init__ de las clases que vamos a utilizar,
#en clases donde no se ocupen se pueden evitar











