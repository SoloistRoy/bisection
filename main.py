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

    q1.append(float(columns[0]))
    beta1.append(float(columns[1]))
    q2.append(float(columns[2]))
    beta2.append(float(columns[3]))

beta = 2e-11
q=40.0

def f(z) :
    return 1 + beta - z - (q * beta / z) * ( (z-beta) /(z+beta) )

def imprimir( raiz , archivoSalida ) :
    archivo = open( sys.argv[2] , 'w' )
    archivo.write( str( raiz ) + '\t' + str( f(raiz) ) + '\n' )
    archivo.close() 

for i in range( len(q1) ):
    resultado1.append( biseccion.solucion( f1 , 0.1 , 2.0 ) ) 
    


resultado = biseccion.solucion( f , 0.1 , 2.0 )
imprimir( resultado, 'salida.txt' )
