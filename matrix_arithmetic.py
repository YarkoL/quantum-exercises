#!/usr/bin/env python2

import complex_arithmetic as ar

testA = [[(1, -1), (3, 0)], [(2, 2), (4, 1)]]
testB = [[(2, 1), (-3, 1)], [(0, -4), (5, -2)]]
testS = (3,-1)

def start(): 
  print("Let's do operations using complex matrices.")
 
  m = input("Number of rows : ")
  n = input("Number of cols : ")
  
  choice = input("Select (1) Addition (2) Inverse (3) Scalar multiplication   ")
  if choice == 1:
    A = init_matrix(m,n)
    B = init_matrix(m,n)
    
    print ("Enter first " + str(n) + "X" + str(m) + " matrix")
    A = populate_matrix(A)
    print(A)

    print ("Enter second " + str(n) + "X" + str(m) + " matrix")
    B = populate_matrix(B)
    print(B)
    print

    M = add(A,B)
    print format(A), "+" , format(B) , "=" , format(M)
    return

  if choice == 2:
    
    A = init_matrix(m,n)
    print ("Enter " + str(n) + "X" + str(m) + " matrix")
    A = populate_matrix(A)
    print(A)
    print

    inv = invert(A)
    zeroes = add(A,inv)
    print format(A), "+" , format(inv) , "=" , format(zeroes)
    return
  if choice == 3:
    A = init_matrix(m,n)
    print ("Enter " + str(n) + "X" + str(m) + " matrix")
    A = populate_matrix(A)
    print(A)
    print

    a = input("Give real part of the complex scalar : ")
    b = input("Give imaginary part of the complex scalar : ")
    scalar = (a,b)

    result = scalar_multiply(scalar,A)
    print ar.format(scalar), "*", format(A), "=", format(result)
    return
  print ("Invalid choice")
  
def init_matrix(cols,rows):
  A = [(0,0)] * cols
  for i in range(cols):
    A[i] = [(0,0)] * rows
  return A

def populate_matrix(A):
  rows = len(A)
  cols = len(A[0])
  for j in range(rows):
    for k in range(cols):
      a = input("Give real part of the complex number at " + str(j) + "," + str(k) + " : ")
      b = input("Give imaginary part of the complex number at " + str(j) + "," + str(k) + " : ")
      A[j][k] = (a,b)
  return A

def format(A):
  rows = len(A)
  cols = len(A[0])
  res = A
  for j in range(rows):
    for k in range(cols):
      res[j][k] = ar.format(A[j][k])
  return res

def add(A,B):
  rows = len(A)
  cols = len(A[0])
  res = init_matrix(rows,cols)
  for j in range(rows):
    for k in range(cols):
      res[j][k] = ar.add(A[j][k],B[j][k])
  return res

def invert(A):
  rows = len(A)
  cols = len(A[0])
  res = init_matrix(rows,cols)
  for j in range(rows):
    for k in range(cols):
      a,b = A[j][k]
      a *= -1
      b *= -1
      res[j][k] = (a,b)
  return res

def scalar_multiply(s,A):
  rows = len(A)
  cols = len(A[0])
  res = init_matrix(rows,cols)
  for j in range(rows):
    for k in range(cols):
      res[j][k] = ar.multiply(s,A[j][k])  
  return res

if __name__ == '__main__':
  start()
