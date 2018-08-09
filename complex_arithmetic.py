#!/usr/bin/env python2

from __future__ import division
import math

def start():
  print "Let's perform operations on complex numbers!"
  
  print
  a1 = input("Enter real part of the first complex number : ")
  b1 = input("Enter imaginary part of the first complex number : ") 
  c1 = (round(a1,3),round(b1,3))
  printout(c1)
  print
  a2 = input("Enter real part of the second complex number : ")
  b2 = input("Enter imaginary part of the second complex number : ") 
  c2 = (round(a2,3),round(b2,3))
  printout(c2)
  print
  print c1,"+",c2,"=",format(add(c1,c2))
  print
  print c1,"-",c2,"=",format(substract(c1,c2))
  print
  print c1,"*",c2,"=",format(multiply(c1,c2))
  print
  print c1,"/",c2,"=",format(divide(c1,c2))
 
def add(c1,c2):
  a1,b1 = c1
  a2,b2 = c2
  a = a1 + a2
  b = b1 + b2
  return (round(a,3), round(b,3))

def substract(c1,c2):
  a1,b1 = c1
  a2,b2 = c2
  a = a1 - a2
  b = b1 - b2
  return (round(a,3), round(b,3))

def multiply(c1,c2):
  a1,b1 = c1
  a2,b2 = c2
  a = a1 * a2 - b1 * b2
  b = a1 * b2 + a2 * b1
  return (round(a,3), round(b,3))

def scalar_multiply(s,c):
  a,b = c
  return (s*a,s*b)

def divide(c1,c2):
  a1,b1 = c1
  a2,b2 = c2
  mod_sq = modulus_squared(c2)
  a = ( a1 * a2 + b1 * b2 ) / mod_sq
  b = ( a2 * b1 - a1 * b2 ) / mod_sq
  return (round(a,3),round(b,3))

def modulus_squared(c):
  a,b = c
  res = float(a)**2 + float(b)**2
  return round(res,3) 

def conjugate(c):
  a,b = c
  b *= -1
  return (a,b)

def format(c):
  a,b = c
  a_str = str(a)
  b_str = str(b)
  c_str = "a+bi"
  c_str = c_str.replace("a",a_str)
  if b < 0:
    c_str = c_str.replace("+","-")
    b_str = b_str[1:]
  if b == 1:
    b_str = ""
  c_str = c_str.replace("b", b_str)
  return c_str  

def printout(c):
  print format(c)
  print "Conjugate : ", format(conjugate(c))
  print "Modulus : ", round(math.sqrt(modulus_squared(c)),3)

if __name__ == '__main__':
  start()
