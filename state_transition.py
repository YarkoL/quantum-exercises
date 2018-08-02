#!/usr/bin/env python2

import real_operations as reals

testing = False

def start():
  if testing:
    pass
  else:  	
    n = input("Enter the length of the state vector  ")
    X = reals.init_matrix(1,n)
  
    print ("Enter the wiring of the system ")
    M = reals.init_matrix(n,n)
    for i in range(n):
      j = input("Slot " + str(i) + " goes to   ")
      M[i][j] = 1
    print M 

    print ("Enter inital state")
    X = reals.populate_matrix(X)
    print ("INITIAL")
    print X

  for i in range(10):
    print i
    X = reals.matrix_multiply(X,M)
    print X


def apply_transition(M,X):
  n = len(X[0])
  X1 = reals.init_matrix(1,n)
  for i in range(n):
    for j in range(n):
      mx = M[i][j] * X[0][j]
      X1[0][i] += mx 
  return X1     	

if __name__ == '__main__':
  start()
