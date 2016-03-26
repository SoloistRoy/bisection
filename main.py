#!/usr/bin/python
# coding: utf-8

import biseccion
import sys

archivoEntrada = open(sys.argv[1], 'r')

q1=[]
beta1=[]
q2=[]
beta2=[]
resultado1=[]
resultado2=[]

#Leer lineas del archivo
for line in archivoEntrada:
    line = line.strip()
    columns = line.split() 

    q1.append(float(columns[1]))
    beta1.append(float(columns[0]))
    q2.append(float(columns[3]))
    beta2.append(float(columns[2]))

def soave( z , q , beta ):
    return 1 + beta - z - ( (q * beta / z) * ( (z-beta) / (z+beta) ) )

def imprimir( raiz1 , raiz2 ) :
    archivo = open( sys.argv[2] , 'w' )
    for i in range(len(raiz1)):
        archivo.write( str( raiz1[i] ) + '\t' + str( raiz2[i] ) + '\n' )
    archivo.close() 

for i in range( len(q1) ):
    resultado1.append( biseccion.solucion( soave , 0.1 , 2.0 , q1[i] , beta1[i] ) ) 
    resultado2.append(0)

imprimir( resultado1, resultado2 )    
