#!/usr/bin/env python2

from __future__ import division
import real_operations as reals

testing = False

def start():
  if testing:
    M = [[0.0,0.5,0.5,0.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.333,0.333,0.333,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.333,0.333,0.333],[0.0,0.0,0.0,1.0,0.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,1.0,0.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,1.0,0.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,1.0,0.0],[0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0]]
    X = [[1,0,0,0,0,0,0,0]]
  else:  	
    n = input("Enter the length of the state vector  ")
    X = reals.init_matrix(1,n)
  
    print ("Enter the wiring of the system ")
    M = reals.init_matrix(n,n)
    for i in range(n):
    	for j in range(n):
      	  p = input("Probability of " + str(i) + " changing to " + str(j) + "  ")
          M[i][j] = round(float(p),3)
    print M 

    print ("Enter inital state")
    X = reals.populate_matrix(X)
    print ("INITIAL")
    print X

  for i in range(10):
    print i
    X = reals.matrix_multiply(X,M)
    print X

  M_i = M
  for i in range(10):
    print i
    M_i = reals.matrix_multiply(M,M_i)
    print M_i
        
if __name__ == '__main__':
  start()
