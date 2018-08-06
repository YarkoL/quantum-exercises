#!/usr/bin/env python2

from __future__ import division
import math
import matrix_arithmetic as mat

testing = False

def start():
  if testing:
    pass
  else:  	
    n = input("Enter the length of the state vector  ")
    X = mat.init_matrix(1,n)
  
    print ("Enter the wiring of the system ")
    M = mat.init_matrix(n,n)
    for i in range(n):
    	for j in range(n):
      	  print("Probability of " + str(i) + " changing to " + str(j) + "  ")
          a = input("real part  : ")
          b = input("imaginary part  : ")
          M[i][j] = (round(a,3), round(b,3))
    print M 

    print ("Enter inital state")
    X = mat.populate_matrix(X)
    print ("INITIAL")
    print X

  for i in range(10):
    print i
    X = mat.matrix_multiply(X,M)
    print X

  M_i = M
  for i in range(10):
    print i
    M_i = mat.matrix_multiply(M,M_i)
    print M_i
        
if __name__ == '__main__':
  start()
