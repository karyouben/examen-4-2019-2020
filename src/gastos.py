# -*- coding: utf-8 -*-
'''
Created on 25 ene 2022

@author: willi
'''
from collections import namedtuple
from collections import Counter
import csv
from parsers import *
import statistics

Gasto = namedtuple('Gasto', 'num_Gasto,usuario,concepto,destinatario,cantidad,fecha')

def lee_gastos(fichero):
    with open(fichero, encoding='utf-8') as f:
        lector= csv.reader(f)
        next(lector)
        res=[]
        for num_gastos,usuario,concepto,destinatario,cantidad,fecha in lector:
            tupla_gastos = Gasto(int(num_gastos),usuario,concepto,destinatario,float(cantidad),parsea_fecha(fecha))
            res.append(tupla_gastos)
    return res

def pagadores_y_conceptos(gastos): 
    conj_pag = {t.usuario for t in gastos}
    conj_concep = {t.concepto for t in gastos}
    res1 = sorted(conj_pag)
    res2 = sorted(conj_concep)
    return ((res1,res2))

def entre_fechas(fecha,fecha1=None,fecha2=None):
    if fecha1:
        fecha1 = datetime.strptime(fecha1,'%d/%m/%Y').date()
    if fecha2:
        fecha2 = datetime.strptime(fecha2,'%d/%m/%Y').date()
    res=True
    if fecha1== None and fecha2==None:
        res=True
    elif fecha1 ==None:
        res= fecha<=fecha2
    elif fecha2 ==None:
        res= fecha>= fecha1
    else:
        res= fecha1<=fecha<=fecha2
    return res

def total_importe(gastos,fecha1=None,fecha2=None):
    return sum(t.cantidad for t in gastos if entre_fechas(t.fecha,fecha1,fecha2))

def conceptos_menos_gastos(gastos):
    dicc = agrupa_por_conceptos(gastos)
    minimo = min(dicc.values())
    return[clave for clave,valor in dicc.items() if valor == minimo]

def agrupa_por_conceptos(gastos):
    dicc= {}
    for t in gastos:
        clave=t.concepto
        if clave in dicc:
            dicc[clave]+= 1
        else:
            dicc[clave]= 1
    return dicc

def pagadores_mayor_importe_medio(gastos,n):
    dicc = dicc_agrupa_pagadores(gastos)
    contador = Counter(t.usuario for t in gastos)
    dicc_media ={}
    for t in dicc:
        dicc_media[t]= dicc[t]/contador[t]
    res =sorted(dicc_media.items(), key = lambda x:x[1], reverse= True)
    if len(dicc_media)>n:
        res=res[:n]
    return res
         

def dicc_agrupa_pagadores(gastos):
    dicc={}
    for t in gastos:
        clave = t.usuario
        if clave in dicc:
            dicc[clave]+= t.cantidad
        else:
            dicc[clave]= t.cantidad
    return dicc

def balance(gastos):
    usuarios = {t.usuario for t in gastos}
    balance_por_usuario = {t:0 for t in usuarios}
    for t in gastos:
        if t.destinatario == 'Todos':
            actualiza_balance(balance_por_usuario, t.cantidad, t.usuario, usuarios)
        else:
            actualiza_balance(balance_por_usuario, t.cantidad, t.usuario, {t.usuario,t.destinatario})
    for usuario,balance in balance_por_usuario.items():
        balance_por_usuario[usuario] = round(balance, 2)
    return balance_por_usuario

def actualiza_balance(balance_por_usuario,cantidad,usuario,beneficiarios):
    balance_por_usuario[usuario]+= cantidad
    cantidad_por_persona = cantidad/len(beneficiarios)
    for t in beneficiarios:
        balance_por_usuario[t]-= cantidad_por_persona