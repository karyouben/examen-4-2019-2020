# -*- coding: utf-8 -*-
'''
Created on 25 ene 2022

@author: willi
'''

from gastos import *



def test_lee_gastos(fichero):
    res = lee_gastos(fichero)
    print(f"Número de registros leídos: {len(res)}")
    print(f"Primer registros: {res[:1]}")
    print("")

def test_pagadores_y_conceptos(gastos):
    res = pagadores_y_conceptos(gastos)
    print(f"Pagadores: {res[0]}")
    print(f"Conceptos: {res[1]}")
    print("")
    
def test_total_importe(gastos,fecha1=None,fecha2=None):
    res = total_importe(gastos,fecha1,fecha2)
    print(f"La cantidad total gastada entre el 5 y el 8 de abril DE 2019 fue : ", total_importe(gastos,'05/04/2019','08/04/2019') )
    print("La cantidad total gastada fue: ", total_importe(gastos))
    print("")
    
def test_conceptos_menos_gastos(gastos):
    res = conceptos_menos_gastos(gastos)
    print(f"Los conceptos con menos gastos registrados son: {res}")
    print("")
    
def test_pagadores_mayor_importe_medio(gastos,n):
    res = pagadores_mayor_importe_medio(gastos,n)
    print(f"Los tres pagadores con un mayor importe medio en sus gastos son: {res}")
    print("")

def test_balance(gastos):
    res = balance(gastos)
    print(f"El balance final de gastos es el siguiente: ")
    for t in sorted(res):
        print(t,"->",res[t])
    print("")
       
def muestra_diccionario(dicc):
    for clave,valor in dicc.items():
        print(f"{clave}-> {valor}")

def main():
    fichero = '../data/gastos.csv'
    GASTOS = lee_gastos(fichero)
    test_lee_gastos(fichero)
    test_pagadores_y_conceptos(GASTOS)
    test_total_importe(GASTOS)
    test_conceptos_menos_gastos(GASTOS)
    test_pagadores_mayor_importe_medio(GASTOS, 3)
    test_balance(GASTOS)
    
if __name__=="__main__":
    main()