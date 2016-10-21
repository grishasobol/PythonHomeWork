import scipy as sc
import numpy as np
import scipy.linalg as lin

matrix = sc.random.normal(0, 1, [5, 5])
print matrix
print 
eigenvalues, eigevectors = lin.eig(matrix)
print eigenvalues,
print eigevectors
id = sc.eye(5, 5)
eigevectors = sc.transpose(eigevectors)

for eigenvalue, eigevector in zip(eigenvalues, eigevectors):
	print sc.isclose(sc.dot(matrix, eigevector), sc.dot(eigenvalue, eigevector)).all()