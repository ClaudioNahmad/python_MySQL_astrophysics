+++++++++++++++++++
CURSO PYTHON
+++++++++++++++++++

#Sesión3

#Medir el tiempo en scripts (pues %%time no sirve en los scripts)

import time
N=100
   ...: a=np.random.rand(N,N)
   ...: b=np.zeros_like(a)
   ...: ti=time.time()
   ...: for i in range(N):
   ...:     for j in range(N):
   ...:         b[i,j]=a[i,j]
   ...: tf=time.time()
   ...: 

In [9]: print (tf-ti)
0.00364589691162

def full(N,a,b):
	for i in range(N):
		for j in range(N):
			b[i,j]=a[i,j]
	return b

 t1,b,t2=time.time(),full(N,a,b),time.time()		#en cada time.time() el programa mide el tiempo 

In [12]: t2-t1
Out[12]: 0.003969907760620117

In [13]: x=np.linspace(0,1,3)

In [14]: y=np.linspace(-1,0,2)

In [15]: xc,yc=np.meshgrid(x,y)

In [16]: print xc
[[ 0.   0.5  1. ]
 [ 0.   0.5  1. ]]

In [19]: xm,ym=np.meshgrid(x,y,indexing='ij')

In [20]: print xm
[[ 0.   0. ]
 [ 0.5  0.5]
 [ 1.   1. ]]

In [21]: print ym
[[-1.  0.]
 [-1.  0.]
 [-1.  0.]]

#función where

In [23]: a=np.linspace(0,100,50)

In [24]: index=np.where((a<10)&(a>5))

In [25]: index
Out[25]: (array([3, 4]),)

#arroja los indices en los cuales se cumple la condición que se pidió

In [27]: b=np.random.randint(0,100,5) #da numeros enteros aleatorios en orden: (low,high,size)

In [28]: b
Out[28]: array([18, 40, 78, 55, 17])

c=np.where((b>10)&(b<15))

In [30]: b[c]
Out[30]: array([], dtype=int64)		#es decir, la función where da los indices, no como con mask, que arroja los elementos exactos del array

#operaciones con arrays

a.min()		#regresa valor minimo
a.max()		#regresa valor máximo
a.mean()	#regresa la media
a.sum()		#suma los valores
b[mask].sum()	#se valen las composiciones
b.argmin()	#da el indice del valor minimo
b.argmax	#da el índice del valor máximo

#Arreglos estructurados

In [45]: a=np.array([(3,5.),(2,6)])

In [46]: a
Out[46]: 
array([[ 3. ,  5. ],
       [ 2,  6. ]]) 		#si array encuentra al menos un float, va a convertir a todos los elementos en float

a_struc=np.array([(5.2,8),(3.4,6),(4.1,2)],dtype=[('x',float),('y',int)]) #con dtype se especifica el tipo de variable Y ADEMAS se le asigna un nombre, aquí fue 'x' y 'y', así se evita que el array convierta a todo al tipo de variable con mayor jerarquía
In [50]: print a_struc
[(5.2, 8) (3.4, 6) (4.1, 2)]		#notar que ahora no convirtió a los enteros en flotantes

In [51]: print(a_struc['x'])
[ 5.2  3.4  4.1]

In [52]: print(a_struc['y'])
[8 6 2]

In [53]: print(a_struc[0])
(5.2, 8)

In [54]: a_rec=a_struc.view(np.recarray)

In [55]: a_rec

rec.array([(5.2, 8), (3.4, 6), (4.1, 2)], 
          dtype=[('x', '<f8'), ('y', '<i8')])

#NaN and ANSI values	(Not a Number)

In [57]: a=np.linspace(-2,3,6)

In [58]: b=1./a
/home/claudio/.local/bin/ipython:1: RuntimeWarning: divide by zero encountered in divide
  #!/usr/bin/python                       la division por cero da infinito, en python 'inf' es un NaN(not a number)

In [59]: print b
[-0.5        -1.                 inf  1.          0.5         0.33333333]

In [60]: a.sum()
Out[60]: 3.0

In [61]: b.sum()
Out[61]: inf

In [62]: mask=np.isfinite(b)		#3sta funcion elimina a todos los numeros que no son finitos

In [63]: b[mask]
Out[63]: array([-0.5       , -1.        ,  1.        ,  0.5       ,  0.33333333])

#Escribiendo y leyendo tablas

In [64]: %%writefile data1.dat
    ...: 1 1.3 6 8 star
    ...: 2 6.1 3 4 galaxy
    ...: 3 -5.4 1 6 cluster
    ...: 
Writing data1.dat

In [65]: datafile=open('data1.dat','r')		#lee el archivo desde la terminal


In [65]: datafile=open('data1.dat','r')		#r significa 'read'
In [68]: data=datafile.readlines()		#con esta funcion leemos las lineas del archivo y las pasamos a 'data'

In [69]: data					#notar que .readfiles guarda las líneas en forma de UNA cadena de texto por cada línea
Out[69]: ['1 1.3 6 8 star\n', '2 6.1 3 4 galaxy\n', '3 -5.4 1 6 cluster']

In [70]: datafile.close()			#ya que se hizo lo que queríamos, se DEBE cerrar el archivo

In [72]: data[0]
Out[72]: '1 1.3 6 8 star\n'

In [73]: l1=data[0].split()			#este comando divide la primera entrada, si no se le da argumento, split va a considerar al 'espacio' como el separador

In [74]: l1				
Out[74]: ['1', '1.3', '6', '8', 'star']

In [78]: for row in data:		
    ...:     datos=row.split()
    ...:     print('N={} x={} y={} z={} tipo={}' .format(datos[0],datos[1],datos[2],datos[3],datos[4]))
    ...:    
N=1 x=1.3 y=6 z=8 tipo=star
N=2 x=6.1 y=3 z=4 tipo=galaxy
N=3 x=-5.4 y=1 z=6 tipo=cluster

N=[]
x=[]
tipo=[]


In [83]: for row in data:			#con este for estamos dividiendo los datos en 3 tipos y los estamos metiendo en listas (N,x y tipo)
    ...:     datos=row.split()
    ...:     N.append(int(datos[0]))
    ...:     x.append(float(datos[1]))
    ...:     tipo.append(str(datos[4]))
    ...:     

In [84]: print N
[1, 2, 3]

In [85]: print x
[1.3, 6.1, -5.4]

In [86]: print tipo
['star', 'galaxy', 'cluster']

#otra manera de hacer lo mismo pero con menos líneas de código:

In [87]: N=np.array([int(row.split()[0]) for row in data])

In [88]: x=np.array([float(row.split()[1]) for row in data])

In [89]: tipo=np.array([str(row.split()[4]) for row in data])	#sin embargo, como tipo está hecho de cadenas, no es necesario convertirlo en array:

tipo=[row.split()[4] for row in data]

In [90]: print (N,x,tipo)
(array([1, 2, 3]), array([ 1.3,  6.1, -5.4]), array(['star', 'galaxy', 'cluster'], 
      dtype='|S7'))

#ahora vamos a ver qué pasa con listas que tienen filas u objetos que no nos interesa usar:

In [94]: %%writefle data2.dat
    ...: #estos datos son de prueba
    ...: N f x y tipo
    ...: 1 3.2 5 7 star
    ...: 2 7.1 8 6 galaxy
    ...: 3 -2.1 7 8 cluster
    ...: #4 2.7 6 4 binary
    ...: 

In [100]: datafile=open('data2.dat','r')

In [101]: row=datafile.readline()

In [102]: primer_com=row

In [103]: row=datafile.readline()

In [104]: nombres_var=row

In [105]: nombres_var
Out[105]: 'N f x y tipo\n'

In [106]: primer_com
Out[106]: '#estos datos son de prueba\n'

In [107]: datos_buenos=[]		#lista vacía para ir llenando

In [108]: while True:			
     ...:     row=datafile.readline()
     ...:     if row=='':		#con línea vacía queremos que:
     ...:         break			#'break' rompa el ciclo while
     ...:     
     ...:     if row[0]!='#' and row[0]!='\n':		#si el primer elemento de la línea no es un '#':
     ...:         datos_buenos.append(row.split())	#que se guarde en datos_buenos (con split)
     ...:        

In [109]: print datos_buenos
[['1', '1.3', '6', '8', 'star'], ['2', '6.1', '3', '4', 'galaxy'], ['3', '-5.4', '1', '6', 'cluster']]

In [110]: datafile.close()


#una forma más corta:

In [100]: datafile=open('data2.dat','r')

In [101]: row=datafile.readline()

In [102]: primer_com=row

In [103]: row=datafile.readline()

In [104]: nombres_var=row

In [112]: datos2=[]

In [122]: while row !='':
     ...:     if row[0]!= '#':
     ...:         datos2.append(row.split())
     ...:     row=datafile.readline()
     ...:     

In [123]: datos2
Out[123]: 
 [['1', '1.3', '6', '8', 'star'],
 ['2', '6.1', '3', '4', 'galaxy'],
 ['3', '-5.4', '1', '6', 'cluster']]

#una última manera de hacerlo

In [127]: datafile=open('data2.dat','r')

In [128]: datos3=[]

In [129]: row=datafile.readline()

In [130]: primer_com=row

In [131]: row=datafile.readline()

In [132]: nombres_var=row

In [133]: primer_com
Out[133]: '#estos datos son de prueba\n'

In [134]: nombres_var
Out[134]: 'N f x y tipo\n'

In [135]: for row in datafile:
     ...:     if row[0]!='#':
     ...:         datos3.append(row.split())
     ...:     

In [136]: datafile.close()

In [137]: datos3
Out[137]: 
[['1', '1.3', '6', '8', 'star'],
 ['2', '6.1', '3', '4', 'galaxy'],
 ['3', '-5.4', '1', '6', 'cluster']]

#LA MEJOR MANERA DE HACERLO Y NO MAMADAS:

#loadtxt de numpy

In [141]: b=np.loadtxt('data2.dat',skiprows=2,dtype='i4, f, f, f, U10')

In [142]: b
Out[142]: 
array([(1, 1.2999999523162842, 6.0, 8.0, u'star'),
       (2, 6.099999904632568, 3.0, 4.0, u'galaxy'),
       (3, -5.400000095367432, 1.0, 6.0, u'cluster')], 
      dtype=[('f0', '<i4'), ('f1', '<f4'), ('f2', '<f4'), ('f3', '<f4'), ('f4', '<U10')])

In [143]: b[0]
Out[143]: (1, 1.2999999523162842, 6.0, 8.0, u'star')

#genfromtxt de numpy

In [144]: c=np.genfromtxt('data2.dat',names=True,dtype=None,skip_header=1)	#mucho más facil, skip_header es como skiprows

In [145]: c
Out[145]: 
array([(1, 1.3, 6, 8, 'star'), (2, 6.1, 3, 4, 'galaxy'),
       (3, -5.4, 1, 6, 'cluster')], 
      dtype=[('N', '<i8'), ('f', '<f8'), ('x', '<i8'), ('y', '<i8'), ('tipo', 'S7')])

In [146]: print c
[(1, 1.3, 6, 8, 'star') (2, 6.1, 3, 4, 'galaxy') (3, -5.4, 1, 6, 'cluster')]

In [147]: c['f']
Out[147]: array([ 1.3,  6.1, -5.4])

In [148]: c['N']
Out[148]: array([1, 2, 3])

#una última forma, usando iwal genfromtxt

In [149]: N,f,x,y,tipo=np.genfromtxt('data2.dat',skip_header=2,unpack=True)

In [150]: N
Out[150]: array([ 1.,  2.,  3.])

In [151]: f
Out[151]: array([ 1.3,  6.1, -5.4])

In [152]: x
Out[152]: array([ 6.,  3.,  1.])

In [153]: y
Out[153]: array([ 8.,  4.,  6.])

In [154]: tipo
Out[154]: array([ nan,  nan,  nan])

