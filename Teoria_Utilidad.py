#  -*- coding: utf-8 -*-
from re import split

Lista1 = []
Lista2 = []


def opcion():
	opcion = input("\nEscriba o pegue la opcion completa y despues press enter para continuar:\n")
	return opcion


def calcular(opcion1, valoresLista):
	rest = split('\D+',opcion1)
	for i in rest:
		valoresLista.append(i)
	print('Los valores de la opcion ingresada son:',valoresLista)

ciclo = 1

while True:
	valoresLista = Lista1
	calcular(opcion(), valoresLista)
	ciclo = ciclo + 1

	if ciclo == 2:
		valoresLista = Lista2
		calcular(opcion(), valoresLista)
		break


opc1 = int(Lista1[1])*(int(Lista1[2])/100) + (-(int(Lista1[3]))*(int(Lista1[4]) /100))
opc2 = int(Lista2[1])*(int(Lista2[2])/100) + (-(int(Lista2[3]))*(int(Lista2[4]) /100))

if opc1 > opc2:
	print("\nLa  Opcion(A) tiene mayor utilidad\n")
	print(opc1)
else :
	print("\nLa Opcion(B) tiene mayor utilidad\n")
	print(opc2)

if opc1 == opc2:
	print("La dos Opciones tinen la misma utilidad")
	print(opc1,'-misma utilidad-',opc2)
