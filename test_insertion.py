# coding=utf-8
# Python3

#
# DESCRIPCION: Aplicación del algoritmo de ordenamiento asertionsort.
#

# Autores: 
#	Gregory Muñoz, Ka Shing Fung Ng 
#
# Ultima modificacion: 20/09/2019
#

from insertion import insertion_sort

with open('dato.txt', 'r') as f:
    A = f.readlines()
    f.closed

array_size = len(A)

insertion_sort(A, array_size)