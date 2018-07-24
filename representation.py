#!/usr/bin/env python2

from __future__ import division
import math

def start():
  choice = input("If you want to convert polar coordinates to cartesian, hit 1. To convert cartesian to polar, hit 2   -> ")
  if choice == "1":
    polar2cartesian()
  else:
    cartesian2polar()
    
def polar2cartesian():
  modulus = input("Modulus : ")
  angle = input("Angle in degrees : ")
  angle = degrees2radians(angle)
  print " real part : ", modulus * math.cos(angle)
  print " imaginary part : ", modulus * math.sin(angle)

def cartesian2polar():
  re = input("Real part : ")
  im = input("Imaginary part : ")
  print "Modulus : ", math.sqrt(re**2 + im**2)
  print "Angle in degrees: ", radians2degrees(math.atan2(im,re))
  
def degrees2radians(angle):
  return angle * math.pi / 180

def radians2degrees(angle):
  return angle * 180 / math.pi

if __name__ == '__main__':
  start()
