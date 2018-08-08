#!/usr/bin/env python2
from __future__ import division
import matrix_arithmetic as mat
import complex_arithmetic as ar
import math
testing = True

def start():
  if testing:
  	V1 = [[(0.0, 0.707), (-0.707, 0.0)]]
  	V2 = [[(0.707, 0.0), (0.0, 0.707)]]
  else:  	
    print("Let's calculate things based on inner product of two complex vectors.")
    n = input("Length of the vectors ")
    V1 = mat.init_matrix(1,n)
    V2 = mat.init_matrix(1,n)
    print ("Enter first vector")
    V1 = mat.populate_matrix(V1)
   
    print ("Enter second vector")
    V2 = mat.populate_matrix(V2)
    
  print(V1)  
  print("Length  : " + str(length(V1)))  
  print(V2)
  print("Length : " + str(length(V2)))
  inner = inner_product(V1,V2)
  print("-------------------- ")
  print("Inner product ")
  print(ar.format(inner))
  print("-------------------- ")
  print("Distance")
  print (distance(V1,V2))
   
def inner_product(A,B):
  res = (0,0)
  n = len(A[0])
  A_ = mat.conjugate(A)	
  for i in range(n):
  	p = ar.multiply(A_[0][i],B[0][i])
  	res = ar.add(res,p)
  return res
  
def length(A):
  (re,im) = inner_product(A,A)
  return round(math.sqrt(re),3)

def distance(A,B):
  diff = mat.substract(A,B)
  return length(diff)

if __name__ == '__main__':
  start()
