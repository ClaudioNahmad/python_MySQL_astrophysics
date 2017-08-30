#!/usr/bin/env python
#-*- coding:utf-8 -*-

#-----------------------------------------------------------------------------------------------------
#Código por:		Claudio Nahmad Arcaraz
#fecha:			30/agosto/2017
#tarea:			2

#LIBRERIAS--------------------------------------------------------------------------------------------
import numpy as np
import scipy as sp  				#estas lineas importan las librerias necesarias

#CONSTANTES/UNIDADES------------------------------------------------------------------------------

sii6716=[2e33,2e34,2.3e34,4.5e34]
sii6731=[1.3e33,2.9e34,6.7e34,5.2e34]
a=np.array(sii6716)
b=np.array(sii6731)

T=1.2e4

#ECUACIONES FISICAS---------------------------------------------------------------------------------------

t=T/1e4	

def ne(x,t):
	ne=1e4*x*(t**(0.5))		#densidad electrónica
	return ne

def R(x):
	R=1.49*((1+3.77*x)/(1+12.8*x))
	return R

#---------------------------------------------------------------------------------------------------------

print('Este programa calculará la densidad electrónica (ne) de una región ionizada')
print('Se tienen dos conjuntos de valores: [SII]6716 y [SII]6731: \n')
print('[SII]6716= {} \n[SII]6731= {}'.format(a,b))

c=a/b			#hace la división de valores
mask1=(c>0.4)&(c<1.5)	#impone la condición de 0.4<R<1.5
d=c[mask1]		#este nuevo array contiene solo los valores de R que cumplen con la condición anterior
print ('\nSi R=[SII]6716/[SII]6731 con 0.4<R<1.5, solo los valores {} lo cumplen' .format(d))

R2=np.array([])		#este array se llenará con los cálculos de R dado un valor inicial de x			
#---------------------------------------------------------------------------------------------------------


eleccion=int(raw_input('\n\n¿Para qué valor de R deseas calcular ne? para 0.6896 presiona 1, para 0.8653 presiona 2: '))

if eleccion == 1:

	x=float(raw_input('\nPara explorar el valor de x ingresa un valor inicial (real) de x entre 0 y 1: '))
	#se escoge el intervalo [0,1] pues es el más representativo de la función R: mientras x tiende a 0, R 	tiende a ~1.49; si x tiende a infinito, R tiende a ~0.41, sin embargo, a partir de x~1 R se parece mucho a 0.4xxxx

	print('Para x={}, el valor de R es: R(x)={}' .format(x,R(x)))	
	check1=(x>=0.3)&(x<=1)	
	check2=(x>=0)&(x<=0.1)		#se está dividiendo al intervalo [0,1] en:
	check3=(x>0.1)&(x<=0.2)		#----- [0,0.1](0.1,0.2](0.2,0.3)[0.3,1] ----------
	check4=(x>0.2)&(x<0.3)		#-------chk2----chk3-----chk4----chk1-------------

	print ('\n\nx E [0.3,1] : {}' .format(check1))
	print ('x E [0,0.1] : {}' .format(check2))
	print ('x E (0.1,0.2] : {}' .format(check3))
	print ('x E (0.2,0.3) : {}' .format(check4))

	continua=str(raw_input("\n¿Deseas continuar? <si/no>: "))

	check5=(R(x)>0.689654)&(R(x)<0.689656)		#esta condicion se impone para hacer que la iteración llegue lo más cerca posible al valor esperado de R
	while continua == 'si':
		

		if check1 == True:
	
			check5=(R(x)>0.689654)&(R(x)<0.689656)
			while check5 == False:
				x=x-0.000001		#debido al comportamiento de la función R en el intervalo check1, hay que reducir el valor de x para que se acerque al valor de R
				print (R(x), x, check5)
				check5=(R(x)>0.6800)&(R(x)<0.6899)
	
			if check5 == True:
				continua='no'
				print ('True')
				print ('\n\n-----------------------------\nx= {}' .format(x))
				print ('R(x)= {}' .format(R(x)))		
				print ('ne= {}'.format(ne(x,t)))				
				

		elif check2 == True:
	
			check5=(R(x)>0.689654)&(R(x)<0.689656)
			while check5 == False:
				x=x+0.000001		#de la misma manera, pero ahora hay que sumarle a x para que se acerque al valor de R
				print (R(x), x, check5)
				check5=(R(x)>0.6800)&(R(x)<0.6899)
	
			if check5 == True:
				continua='no'
				print ('True')
				print ('\n\n-----------------------------\nx= {}' .format(x))
				print ('R(x)= {}' .format(R(x)))
				print ('ne= {}'.format(ne(x,t)))	

		elif check3 == True:
	
			check5=(R(x)>0.689654)&(R(x)<0.689656)
			while check5 == False:
				x=x+0.000001		#los intervalos check3 y check4 se encuentran en una zona "crítica" donde el valor de R es muy cercano al esperado, pero no lo suficiente
				print (R(x), x, check5)
				check5=(R(x)>0.689654)&(R(x)<0.689656)
	
			if check5 == True:
				continua='no'
				print ('True')
				print ('\n\n-----------------------------\nx= {}' .format(x))
				print ('R(x)= {}' .format(R(x)))
				print ('ne= {}'.format(ne(x,t)))

		elif check4 == True:
	
			check5=(R(x)>0.689654)&(R(x)<0.689656)
			while check5 == False:
				x=x-0.000001
				print (R(x), x, check5)
				check5=(R(x)>0.689654)&(R(x)<0.689656)
	
			if check5 == True:
				continua='no'
				print ('True')
				print ('\n\n-----------------------------\nx= {}' .format(x))
				print ('R(x)= {}' .format(R(x)))
				print ('ne= {}'.format(ne(x,t)))

#--------------------------------------------------------------------------------------------------------------
	
elif eleccion == 2:

	x=float(raw_input('\nPara explorar el valor de x ingresa un valor inicial (real) de x entre 0 y 1: '))

	print('Para x={}, el valor de R es: R(x)={}' .format(x,R(x)))	
	check1=(x>=0.3)&(x<=1)	
	check2=(x>=0)&(x<=0.1)		
	check3=(x>0.1)&(x<=0.2)	
	check4=(x>0.2)&(x<0.3)		
	
	print ('\n\nx E [0.3,1] : {}' .format(check1))
	print ('x E [0,0.1] : {}' .format(check2))
	print ('x E (0.1,0.2] : {}' .format(check3))
	print ('x E (0.2,0.3) : {}' .format(check4))

	continua=str(raw_input("\n¿Deseas continuar? <si/no>: "))
	while continua == 'si':
		check5=(R(x)>0.86537)&(R(x)<0.86539)
	

		if check1 == True:
	
			check5=(R(x)>0.86537)&(R(x)<0.86539)
			while check5 == False:
				x=x-0.00001
				print (R(x), x, check5)
				check5=(R(x)>0.86537)&(R(x)<0.86539)			
	
			if check5 == True:
				continua='no'
				print ('True')
				print ('\n\n-----------------------------\nx= {}' .format(x))
				print ('R(x)= {}' .format(R(x)))
				print ('ne= {}'.format(ne(x,t)))				
				
		elif check2==True:
	
			check5=(R(x)>0.86537)&(R(x)<0.86539)
			while check5 == False:
				x=x+0.00001
				print (R(x), x, check5)
				check5=(R(x)>0.86537)&(R(x)<0.86539)
	
			if check5 == True:
				continua='no'
				print ('True')
				print ('\n\n-----------------------------\nx= {}' .format(x))
				print ('R(x)= {}' .format(R(x)))
				print ('ne= {}'.format(ne(x,t)))	
	
		elif check3==True:
	
			check5=(R(x)>0.86537)&(R(x)<0.86539)
			while check5 == False:
				x=x-0.00001
				print (R(x), x, check5)
				check5=(R(x)>0.86537)&(R(x)<0.86539)
	
			if check5 == True:
				continua='no'
				print ('True')
				print ('\n\n-----------------------------\nx= {}' .format(x))
				print ('R(x)= {}' .format(R(x)))
				print ('ne= {}'.format(ne(x,t)))

		elif check4==True:
	
			check5=(R(x)>0.86537)&(R(x)<0.86539)
			while check5 == False:
				x=x+0.00001
				print (R(x), x, check5)
				check5=(R(x)>0.86537)&(R(x)<0.86539)
				continua='si'
	
			if check5 == True:
				continua='no'
				print ('True')
				print ('\n\n-----------------------------\nx= {}' .format(x))
				print ('R(x)= {}' .format(R(x)))
				print ('ne= {}'.format(ne(x,t)))





		

		

			

