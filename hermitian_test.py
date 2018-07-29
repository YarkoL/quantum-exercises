#!/usr/bin/env python2

import matrix_arithmetic as mat

testA = [[(7,0),(6,5)],[(6,-5),(2,0)]]
testing = False

def start():
  if testing:
  	A = testA
  else:	
    print "Test if a complex nxn-matrix is hermitian"
    n = input("Enter dimension n  :  ")
    A = mat.init_matrix(n,n)
    A = mat.populate_matrix(A)
  print("Is this matrix hermitian : ", is_hermitian(A))

def is_hermitian(A):
  A_transposed = mat.transpose(A)
  A_conjugated = mat.conjugate(A)
  return A_transposed == A_conjugated 	   

if __name__ == '__main__':
  start()
