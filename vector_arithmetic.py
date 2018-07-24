#!/usr/bin/env python2

import complex_arithmetic as ar

n = 2 #vector length

def start(): 
  print("Let's do operations using complex vectors of length " + str(n))
  choice = input("Select (1) Addition (2) Inverse (3) Scalar multiplication   ")
  if choice == 1:
    print ("Enter first vector")
    v1 = input_vector()
    print ("Enter second vector")
    v2 = input_vector()
    v = add(v1,v2)
    #print v1," + ",v2," = ",v
    print format(v1), "+" , format(v2) , "=" , format(v)
    return
  if choice == 2:
    print ("Enter vector")
    v = input_vector()
    inv = invert(v)
    zeroes = add(v,inv)
    print format(v), "+" , format(inv) , "=" , format(zeroes)
    return
  if choice == 3:
    print ("Enter vector")
    v = input_vector()   
    a = input("Give real part of the complex scalar : ")
    b = input("Give imaginary part of the complex scalar : ")
    scalar = (a,b)
    result = scalar_multiply(scalar,v)
    print ar.format(scalar), "*", format(v), "=", format(result)
    return
  print ("Invalid choice")

def add(v1,v2):
  vec = []
  for i in range(n):
    c = ar.add(v1[i],v2[i])
    vec.append(c)
  return vec

def invert(v):
  vec = []
  for c in v:
    a,b = c
    a *= -1
    b *= -1
    vec.append((a,b))
  return vec

def scalar_multiply(s,v):
  vec = []
  for c in v:
    product = ar.multiply(s,c)
    vec.append(product)
  return vec

def input_vector():
  vec = []
  for i in range(n):
    a = input("Give real part of the complex number at index " + str(i) + " : ")
    b = input("Give imaginary part of the complex number at index " + str(i) + " : ")
    vec.append((a,b))
  return vec

def format(v):
  vec = []
  for c in v:
    vec.append(ar.format(c))
  return vec

if __name__ == '__main__':
  start()
