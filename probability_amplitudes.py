from __future__ import division
import matrix_arithmetic as mat
import complex_arithmetic as ar
import vectors_inner_product as inner
import math

x = [[(2.0, -1.0), (0.0, 2.0), (1.0, -1.0), (1.0, 0.0), (0.0, -2.0), (2.0, 0.0)]]

testing = False

def start():
  if testing:
    ket = x
    n = len(x[0])	
  else:  
    print("Let's calculate some probabilities in a simple quantum system")
    n = input("Enter the number of states in a system  :")
    ket = mat.init_matrix(1,n) 	
    print("Enter a (ket) state vector")
    mat.populate_matrix(ket)
    print(ket)
  p = get_probabilities(ket)
  print("--------------------------------------------------")
  print("Norm of ket " + str(round(norm(ket),4)))
  for i in range(n):
  	print("The probability of finding particle at state " + str(i) + " is " + str(round(p[0][i],4)))
  print("--------------------------------------------------")
  answer = raw_input("Calculate transition amplitude leading to ket? (Hit 'y' to continue) :  ")
  if answer != 'y': 
  	print("Bye")
  	return
  bra = mat.init_matrix(1,n) 	
  print("Enter another (bra) state vector")
  mat.populate_matrix(bra)
  print("--------------------------------------------------")
  print("Norm of bra " + str(round(norm(bra),4)))
  trans = get_transition_amplitude(bra,ket)
  print("Transition amplitude <bra|ket> is " + ar.format(trans))

def get_probabilities(psi):
  n = len(psi[0])
  res = mat.init_matrix(1,n) #result is a vector containing probabilities	
  psi_normalized = normalize(psi)
  for i in range(n):
    res[0][i] = ar.modulus_squared(psi_normalized[0][i])
  return res

def get_transition_amplitude(bra,ket):
  bra_normalized = normalize(bra)
  ket_normalized = normalize(ket)
  res = inner.inner_product(bra_normalized,ket_normalized)
  return res  

def normalize(psi):
  n = len(psi[0])	
  res = mat.init_matrix(1,n) 	
  norm_psi = norm(psi)
  for i in range(n):
  	res[0][i] = ar.scalar_multiply(1/norm_psi,psi[0][i])
  return res

def norm(psi):	
  n = len(psi[0])
  sum_of_moduli_sq = 0
  for i in range(n):
  	mod_sq = ar.modulus_squared(psi[0][i])
  	sum_of_moduli_sq += mod_sq
  return math.sqrt(sum_of_moduli_sq)  	
  
if __name__ == '__main__':
  start()
