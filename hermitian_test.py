#!/usr/bin/env python2

import matrix_arithmetic as mat

testH = [[(7,0),(6,5)],[(6,-5),(2,0)]]
testU = [[(1,0),(0,0)],[(0,0),(0,1)]]
testM = [[(5,0),(2,-1)],[(0,0),(4,5)]]
testing = False

def start():
  if testing:
  	A = testM
  else:	
    print "Test if a complex nxn-matrix is hermitian or unitary"
    n = input("Enter dimension n  :  ")
    A = mat.init_matrix(n,n)
    A = mat.populate_matrix(A)
  print(A)  
  print("Is this matrix hermitian : " + str(is_hermitian(A)))
  print("Is this matrix unitary : " + str(is_unitary(A)))

def is_hermitian(A):
  A_transposed = mat.transpose(A)
  A_conjugated = mat.conjugate(A)
  return A_transposed == A_conjugated 	  

def is_unitary(A):
  I = mat.get_identity_matrix(len(A))
  A_dagger = mat.conjugate(mat.transpose(A))   
  P = mat.matrix_multiply(A_dagger, A)
  return mat.equals(P,I)

if __name__ == '__main__':
  start()
