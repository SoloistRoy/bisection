#!/usr/bin/python
# coding: utf-8

MAX_ITERACIONES = int(1e7);
TOLERANCIA = 1e-16;

def mismoSigno( a , b ):
    return a * b > 0

def solucion( funcion , minimo, maximo , *extraArgs ):

    puntoMedio = 0.5 * ( minimo + maximo )
    assert (not mismoSigno( funcion(minimo, *extraArgs ) , funcion(maximo, *extraArgs ) )) , "Error: Interválo inválido."

    iteraciones = 0

    while abs(funcion(puntoMedio, *extraArgs )) > TOLERANCIA and 0.5 * ( maximo - minimo ) > TOLERANCIA :
        puntoMedio = 0.5 * ( minimo + maximo )
        if mismoSigno( funcion(minimo, *extraArgs ) , funcion(puntoMedio, *extraArgs ) ):
            minimo = puntoMedio
        else :
            maximo = puntoMedio
        iteraciones+=1
        assert (iteraciones < MAX_ITERACIONES), "Error: Número Máximo de Iteraciones."

    return puntoMedio
