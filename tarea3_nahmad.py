#!/usr/bin/env python
#-*- coding:utf-8 -*-

#-----------------------------------------------------------------------------------------------------
#Código por:		Claudio Nahmad Arcaraz
#fecha:			6/septiembre/2017
#tarea:			3

#LIBRERIAS--------------------------------------------------------------------------------------------
import numpy as np
import scipy as sp  				#estas lineas importan las librerias necesarias
from numpy import isnan
import math 
from math import fabs

#-----------------------------------------------------------------------------------------------------

print('Este programa leerá el archivo SATURN.dat y hará operaciones con sus elementos')

#nombre=str(raw_input('\n¿Qué nombre quieres asignarle a la variable donde se guardarán los datos de SATURN.dat?: '))
saturn=np.genfromtxt('SATURN.dat',names=True,dtype=float,skip_header=3,filling_values=0.0)

Time=saturn['Time']
a=saturn['a']
Q=saturn['Q']
e=saturn['e']
peri=saturn['peri']
i=saturn['i']
M=saturn['M']
node=saturn['node']
oblq=saturn['oblq']
q=saturn['q']
r=saturn['r']
x=saturn['x']
y=saturn['y']
z=saturn['z']
vx=saturn['vx']
vy=saturn['vy']
vz=saturn['vz']

where_nans=isnan(y)
condicion1=np.where((Time>3)&(Time<25))

x2=x[condicion1]
y2=y[condicion1]

distancias=(x2-y2)
print(distancias)

distancias2=[]

for i in distancias:
	i=fabs(i)
	distancias2.append(i)

distancias=np.array(distancias2)

dmin=distancias.min()
dmax=distancias.max()

print (distancias)
#print (len(distancias))
print ('La distancia mínima es: {} '.format(dmin))
print ('La distancia máxima es: {} '.format(dmax))
