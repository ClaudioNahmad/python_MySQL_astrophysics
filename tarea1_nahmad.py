#!/usr/bin/env python
#-*- coding:utf-8 -*-

#-----------------------------------------------------------------------------------------------------
#Código por:		Claudio Nahmad Arcaraz
#fecha:			23/agosto/2017
#tarea:			1



#LIBRERIAS--------------------------------------------------------------------------------------------
import numpy as np
import scipy as sp  
import astropy as ap			#estas lineas importan las librerias necesarias
import scipy.constants as spct
import astropy.constants as apct

#IMPORTANTE, se recomienda instalar la librería astropy, para instalarla
#correr en la terminal: > sudo pip install astropy
#sin embargo, no se va a utilizar en este código
#---------------------------------------------------------------------------------------------------------

#UNIDADES-------------------------------------------------------------------------------------------------

G=spct.G
M_sol=1.98847542e+30		
M_jup=1.89818717e+27			#estas unidades se encuentran en kg
M_geo=5.97236473e+24

#ECUACIONES FISICAS---------------------------------------------------------------------------------------

def F(m1,m2,R):
	F=-(G*(m1*m2))/(R**2)		#aquí definimos la función F que calcula la fuerza gravitacional
	return F

fuerzas={}				#aquí abrimos un diccionario vacío

#---------------------------------------------------------------------------------------------------------

print ("Éste programa calculará la fuerza gravitacional Newtoniana entre dos cuerpos")

continua=str(raw_input("\n ¿Deseas continuar? <si/no>: "))
i=0							#esta cifra cuenta el número de cálculos (de fuerza) que llevamos

while continua == "si":					#el while abre un bucle, el cual no termina a menos que el usuario lo indique con cualquier input distinto a "si"

	decision=raw_input("\n\n Si deseas ingresar m1, m2 y R en <kg> y <m> respectivamente, presiona la tecla -a-.\n\n Si deseas utilizar masas astronómicas y distancias en Parsecs presiona la tecla -b-: ")
	#esta es la decision primordial, divide al cálculo en dos disyuntivas: (i) masas y distancias sencillas; (ii) masas y distancias astronómicas
	
	if decision == "a":
		m1=float(raw_input("m1= "))	 
		m2=float(raw_input("m2= "))		#estos tres valores se asignan por el usuario, sus unidades son {mi}=kg y {R}=metros
		R=float(raw_input("R= "))

		print ("m1 = {} kg" .format(m1))	
		print ("m2 = {} kg" .format(m2))	#estas líneas únicamente sirven como retroalimentación al usuario
		print ("R = {} m" .format(R))
		print ("F = {} N" .format(F(m1,m2,R)))	#esta línea arroja el resultado del cálculo de la fuerza

		i=i+1					#esta línea aumenta el contador de número-de-cálculos (i)
		print ("i= {}" .format(i))		
		fuerzas.update({"Fuerza {}" .format(i) : F(m1,m2,R)})		#esta línea agrega el i-esimo resultado de la fuerza al diccionario		
		
		continua=str(raw_input("\n ¿Deseas continuar? <si/no>: "))	#aquí se vuelve a preguntar al usuario si desea seguir calculando fuerzas, redefiniendo la variable "continua"	
		
	elif decision == "b":
		
		mass1=raw_input("\n m1 = {Masa solar, presiona -s- ; Masa de la Tierra, presiona -t- ; Masa de Júpiter, presiona -j-}: ")

		if mass1 == "s":
			m1=float(raw_input("m1= [] M_solares: "))
			m1=m1*M_sol
		elif mass1 == "t":
			m1=float(raw_input("m1= [] M_terrestres: "))
			m1=m1*M_geo
		elif mass1 == "j":
			m1=float(raw_input("m1= [] M_júpiter: "))
			m1=m1*M_jup

		mass2=raw_input("\n m2 = {Masa solar, presiona -s- ; Masa de la Tierra, presiona -t- ; Masa de Júpiter, presiona -j-}: ")
	
		if mass2 == "s":
			m2=float(raw_input("m2= [] M_solares: "))
			m2=m1*M_sol
		elif mass2 == "t":
			m2=float(raw_input("m2= [] M_terrestres: "))
			m2=m1*M_geo
		elif mass2 == "j":
			m2=float(raw_input("m2= [] M_júpiter: "))
			m2=m1*M_jup

		R=float(raw_input("R= {Pc}: "))
		R=R/(3.2408e-17)			#en esta línea solo se transforma de Parsecs a metros

		print ("m1 = {} kg" .format(m1))	
		print ("m2 = {} kg" .format(m2))
		print ("R = {} m" .format(R))
		print ("F = {} N" .format(F(m1,m2,R)))
		
		i=i+1		
		print ("i= {}" .format(i))
		fuerzas.update({"Fuerza {}" .format(i) : F(m1,m2,R)})

		continua=str(raw_input("\n ¿Deseas continuar? <si/no>: "))

else:
	print fuerzas					#aquí mandamos imprimir el diccionario de fuerzas...
	print("\n\n Fin")				# ...antes de cerrar el bucle while y terminar el programa




#REFERENCIAS---------------------------------------------------------------------------------------------------

#https://github.com/VGomezLlanos/Python-lectures-Notebooks/blob/master/Notebooks/intro_Python.ipynb
#https://docs.scipy.org/doc/scipy-0.18.1/reference/constants.html
#http://docs.astropy.org/en/stable/constants/
#https://stackoverflow.com/questions/1024847/add-new-keys-to-a-dictionary
#https://stackoverflow.com/questions/70797/python-user-input-and-commandline-arguments
#https://stackoverflow.com/questions/8114355/loop-until-a-specific-user-input
#https://stackoverflow.com/questions/29873602/python-loop-isnt-waiting-for-users-input
