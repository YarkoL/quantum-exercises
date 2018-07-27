#!/usr/bin/env python2

import complex_arithmetic as ar

testA = [[(3,2),(0,0),(5,-6)],[(1,0),(4,2),(0,1)],[(4,-1),(0,0),(4,0)]]
testB = [[(5,0),(2,-1)],[(0,0),(4,5)],[(7,-4),(2,7)]]

def start(): 
  print("Let's do operations using complex matrices.")
 
  choice = input("Select (1) Addition (2) Inverse (3) Scalar multiplication (4) Transpose (5) Matrix multiplication (6) Conjugate ")
  if choice == 1:
    m = input("Number of rows : ")
    n = input("Number of cols : ")
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
    m = input("Number of rows : ")
    n = input("Number of cols : ")
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
    m = input("Number of rows : ")
    n = input("Number of cols : ")
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
  if choice == 4:
    m = input("Number of rows : ")
    n = input("Number of cols : ")
    A = init_matrix(m,n)
    print ("Enter " + str(n) + "X" + str(m) + " matrix")
    A = populate_matrix(A)
    print(A)
    print
    T = transpose(A)
    print format(T)
    return 
  if choice == 5:
    rowsA = input("Number of rows in the matrix A : ")
    common = input("Number of cols in the matrix A/rows in matrix B: ")
    A = init_matrix(rowsA,common)
    colsB = input("Number of cols in matrix B: ")
    B = init_matrix(common,colsB)
    
    print ("Enter matrix A")
    A = populate_matrix(A)
    print(A)

    print ("Enter matrix B")
    B = populate_matrix(B)
    print(B)
    print
  
    P = matrix_multiply(A,B)
    print format(A), "*" , format(B) , "=" , format(P)
    return   
  if choice == 6:
    m = input("Number of rows : ")
    n = input("Number of cols : ")
    A = init_matrix(m,n)
    print ("Enter " + str(n) + "X" + str(m) + " matrix")
    A = populate_matrix(A)
    print(A)
    print
    A_ = conjugate(A)
    print format(A_)
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

def transpose(A):
  rows = len(A)
  cols = len(A[0])
  res = init_matrix(cols,rows)
  for j in range(cols):
    for k in range(rows):
      res[j][k] = A[k][j]
  return res

def conjugate(A): 
  rows = len(A)
  cols = len(A[0])
  res = init_matrix(rows,cols)
  for j in range(rows):
    for k in range(cols):
      res[j][k] = ar.conjugate(A[j][k])
  return res 

def scalar_multiply(s,A):
  rows = len(A)
  cols = len(A[0])
  res = init_matrix(rows,cols)
  for j in range(rows):
    for k in range(cols):
      res[j][k] = ar.multiply(s,A[j][k])  
  return res

def matrix_multiply(A,B):
  rowsA = len(A)
  colsB = len(B[0])
  res = init_matrix(rowsA,colsB)
  for j in range(rowsA):
    for k in range(colsB):
      el = (0,0)
      for i in range(len(B)):
        p = ar.multiply(A[j][i],B[i][k])
        el = ar.add(el,p)
      res[j][k] = el         
  return res

if __name__ == '__main__':
  start()
