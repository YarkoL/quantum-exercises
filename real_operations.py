#!/usr/bin/env python2

from __future__ import division

def start():
  pass 

def create_vector(n):
  V = init_matrix(1,n)
  populate_matrix(V)
  return V
  
def init_matrix(m,n):
  M = [float(0)] * m
  for i in range(m):
    M[i] = [float(0)] * n
  return M	

def populate_matrix(M):
  rows = len(M)
  cols = len(M[0]) 	
  for i in range(rows):
    for j in range(cols):
      r = input("Enter real number at " + str(i) + "," + str(j) + " : ")
      M[i][j] = float(r)
  return M

def add(A,B):
  rows = len(A)
  cols = len(A[0])
  res = init_matrix(rows,cols)
  for j in range(rows):
    for k in range(cols):
      res[j][k] = round(A[j][k]+B[j][k],3)
  return res

def substract(A,B):
  rows = len(A)
  cols = len(A[0])
  res = init_matrix(rows,cols)
  for j in range(rows):
    for k in range(cols):
      res[j][k] = round(A[j][k]-B[j][k],3)
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
      res[j][k] = round(el,3)         
  return res  

def kronecker_product(A,B):
  m = len(A)
  n = len(A[0])
  p = len(B)
  q = len(B[0])
  res = init_matrix(m*p, n*q)
  for rowA in range(m):
    for colA in range(n):
      for rowB in range(p):
        for colB in range(q):
          res[p*rowA+rowB][q*colA+colB] = round(A[rowA][colA] * B[rowB][colB],3)
  return res  

if __name__ == '__main__':
  start()

