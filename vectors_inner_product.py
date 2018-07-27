#!/usr/bin/env python2

import matrix_arithmetic as mat
import complex_arithmetic as ar
import math

n = 2
def start():
  print("Let's calculate the inner product of two complex " + str(n) +"-vectors.")
  V1 = mat.init_matrix(1,n)
  V2 = mat.init_matrix(1,n)
  print ("Enter first vector")
  V1 = mat.populate_matrix(V1)
  print(V1)
  print("Length : " + str(length(V1)))
  print ("Enter second vector")
  V2 = mat.populate_matrix(V2)
  print(V2)
  print("Length : " + str(length(V2)))
  inner = inner_product(V1,V2)
  print("-------------------- ")
  print("Inner product ")
  print(ar.format(inner))
   
def inner_product(A,B):
  res = (0,0)
  #A_transpose = mat.transpose(A)	
  #print(A_transpose)
  A_ = mat.conjugate(A)	
  for i in range(n):
  	p = ar.multiply(A_[0][i],B[0][i])
  	res = ar.add(res,p)
  return res
  
def length(A):
  (re,im) = inner_product(A,A)
  return math.sqrt(re)

if __name__ == '__main__':
  start()
