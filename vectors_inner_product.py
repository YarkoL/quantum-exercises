#!/usr/bin/env python2

import matrix_arithmetic as mat

n = 2
def start():
  print("Let's calculate the inner product of two complex " + str(n) +"-vectors.")
  V1 = mat.init_matrix(1,n)
  V2 = mat.init_matrix(1,n)
  print ("Enter first vector")
  V1 = mat.populate_matrix(V1)
  print(V1)
  print ("Enter second vector")
  V2 = mat.populate_matrix(V2)
  print(V2)
  V = inner_product(V1,V2)
  print("Inner product : ")
  print(mat.format(V))
   
def inner_product(A,B):
  res = mat.init_matrix(1,n)
  #A_transpose = mat.transpose(A)	
  #print(A_transpose)
  A_dagger = mat.conjugate(A)	
  #print(A_dagger)
  res = mat.matrix_multiply(A_dagger, B)
  return res
  

if __name__ == '__main__':
  start()
