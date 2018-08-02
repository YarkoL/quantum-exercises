#!/usr/bin/env python2

def start():
  n = input("Enter length of vector   ")
  V = create_vector(n)
  print V

def create_vector(n):
  V = init_matrix(1,n)
  populate_matrix(V)
  return V
  
def init_matrix(m,n):
  M = [0] * m
  for i in range(m):
    M[i] = [0] * n
  return M	

def populate_matrix(M):
  rows = len(M)
  cols = len(M[0]) 	
  for i in range(rows):
    for j in range(cols):
      r = input("Enter real number at " + str(i) + "," + str(j) + " : ")
      M[i][j] = r
  return M

def add(A,B):
  rows = len(A)
  cols = len(A[0])
  res = init_matrix(rows,cols)
  for j in range(rows):
    for k in range(cols):
      res[j][k] = A[j][k]+B[j][k]
  return res

def substract(A,B):
  rows = len(A)
  cols = len(A[0])
  res = init_matrix(rows,cols)
  for j in range(rows):
    for k in range(cols):
      res[j][k] = A[j][k]-B[j][k]
  return res    

def matrix_multiply(A,B):
  rowsA = len(A)
  colsB = len(B[0])
  res = init_matrix(rowsA,colsB)
  for j in range(rowsA):
    for k in range(colsB):
      el = 0
      for i in range(len(B)):
        p = A[j][i] * B[i][k]
        el += p
      res[j][k] = el         
  return res  

if __name__ == '__main__':
  start()

