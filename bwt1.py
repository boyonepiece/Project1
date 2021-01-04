# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 11:58:59 2021

@author: Kahn Potter
"""

from __future__ import print_function
from string import printable
from huffman import HuffmanCoding
import timeit

start = timeit.default_timer()

SYMBOLTABLE = list(printable)
SYMBOLTABLE.append('ˆ')
SYMBOLTABLE.append('ƒ')
SYMBOLTABLE.append('‡')

def rotations(t):
    tt = t*2
    return [ tt[i:i+len(t)] for i in range(0, len(t))]
    
def bwm(t):
    return sorted(rotations(t))

def bwt(t):
    return ''.join(map(lambda x: x[-1], bwm(t)))


        
def move2front_encode(strng, symboltable):
    sequence, pad = [], symboltable[::]
    for char in strng:
        indx = pad.index(char)
        sequence.append(indx)
        pad = [pad.pop(indx)] + pad
    return sequence
 

path1 = "test/dickens.txt"
path2 = 'bwt_mtf.txt'


f_in = open(path1,'r')
f_out = open(path2,'w+')


try:
 
    T = f_in.read(1000)
        
    while T != '':
        for i in move2front_encode(bwt(T), SYMBOLTABLE):
            ss = str(i) + ' '
            f_out.write(ss)
        T = f_in.read(1000)
        
    h = HuffmanCoding(path2)
    
    output_path = h.compress()
    h.decompress(output_path)

finally:
    f_in.close()
    f_out.close()


stop = timeit.default_timer()

print('Time: ', stop - start)  
