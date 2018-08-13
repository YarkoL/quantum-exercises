from __future__ import division
import math
import matrix_arithmetic as mat
import hermitian_test as check
import vectors_inner_product as inner

testing = False

def start():
  if testing:
    H = [[(1.0, 0.0), (0.0, -1.0)], [(0.0, 1.0), (2.0, 0.0)]]
    psi = [[(math.sqrt(2)/2,0)],[(0,math.sqrt(2)/2)]]
  else:  
    print("Let's calculate some values related to an observable in a quantum system")
    n = input("Enter the dimension of the hermitian matrix of the observable   : ")
    H = mat.init_matrix(n,n) 	
    mat.populate_matrix(H)
    if check.is_hermitian(H) == False:
  	  print "Not a hermitian matrix! Bye."
  	  return
    print(H)	
    print("Input a ket vector")
    psi = mat.init_matrix(n,1)
    mat.populate_matrix(psi)
  a,b = expected_value(H,psi)
  if b != 0:
    print "Expected value ought to be a real number, but something went wrong"
    print a,b
    return
  print("--------------------------------------------------")
  print("Expected value of observable on ket : " + str(a))
  a,b = variance(H,psi)
  if b != 0:
    print "Variance ought to be a real number, but something went wrong"
    print a,b
    return
  print("--------------------------------------------------")
  print("Variance from expected value  : " + str(a))


def expected_value(H,psi):
  h_psi = mat.matrix_multiply(H,psi)	
  #print h_psi
  return inner.inner_product(mat.transpose(h_psi),mat.transpose(psi))

def variance(H,psi):
  ev = expected_value(H,psi)
  I = mat.get_identity_matrix(len(psi))
  ev_M = mat.scalar_multiply(ev,I)
  demean = mat.substract(H,ev_M)
  demean_sq = mat.matrix_multiply(demean,demean)
  res_intermediate = mat.matrix_multiply(demean_sq,psi)
  psi_conj = mat.conjugate(psi)
  res = mat.matrix_multiply(mat.transpose(psi_conj),res_intermediate)
  return res[0][0]

if __name__ == '__main__':
  start()
