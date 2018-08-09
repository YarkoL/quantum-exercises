from __future__ import division
import matrix_arithmetic as mat
import complex_arithmetic as ar
import vectors_inner_product as inner
import math



def start():
  print("Let's calculate some probabilities in a simple quantum system")
  n = input("Enter the number of states in a system  :")
  ket = mat.init_matrix(1,n) 	
  print("Enter a (ket) state vector")
  mat.populate_matrix(ket)
  p = get_probabilities(ket)
  print("--------------------------------------------------")
  for i in range(n):
  	print("The probability of finding particle at state " + str(i) + " is " + str(round(p[0][i],4)))
  print("--------------------------------------------------")
  answer = raw_input("Calculate transition probability? (Hit 'y' to continue) :  ")
  if answer != 'y': 
  	print("Bye")
  	return
  bra = mat.init_matrix(1,n) 	
  print("Enter another (bra) state vector")
  mat.populate_matrix(bra)
  trans = get_transition_probability(bra,ket)
  print("--------------------------------------------------")
  print("Transition probability <bra|ket> is " + ar.format(trans))

def get_probabilities(psi):
  n = len(psi[0])
  res = mat.init_matrix(1,n) #result is a vector containing probabilities	
  moduli_sq = mat.init_matrix(1,n) #vector containing individual mod_sq of state components
  sum_of_moduli_sq = 0
  for i in range(n):
  	mod_sq = ar.modulus_squared(psi[0][i])
  	moduli_sq[0][i] = mod_sq
  	sum_of_moduli_sq += mod_sq
  for i in range(n):
    res[0][i] = moduli_sq[0][i]/sum_of_moduli_sq
  return res

def get_transition_probability(bra,ket):
  return inner.inner_product(bra,ket)	

if __name__ == '__main__':
  start()
