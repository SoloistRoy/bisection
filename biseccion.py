#!/usr/bin/python
# coding: utf-8

MAX_ITERACIONES = int(1e5);
TOLERANCIA = 1e-15;

def mismoSigno( a , b ):
    return a * b > 0

def solucion( funcion , minimo, maximo ):

    puntoMedio = 0.5 * ( minimo + maximo )
    assert (not mismoSigno( funcion(minimo) , funcion(maximo) )) , "Error: Interválo inválido."

    iteraciones = 0

    while abs(funcion(puntoMedio)) > TOLERANCIA and 0.5 * ( maximo - minimo ) > TOLERANCIA :
    #while abs(funcion(puntoMedio)) > TOLERANCIA  :
        puntoMedio = 0.5 * ( minimo + maximo )
        if mismoSigno( funcion(minimo) , funcion(puntoMedio) ):
            minimo = puntoMedio
        else :
            maximo = puntoMedio
        iteraciones+=1
        assert (iteraciones < MAX_ITERACIONES), "Error: Número Máximo de Iteraciones."

    return puntoMedio
