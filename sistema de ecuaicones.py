import numpy as np

# Definir la matriz A
A = np.array([[52, 30, 18],
              [20, 50, 30],
              [25, 20, 55]])

# Definir el vector b
b = np.array([4800, 5810, 5690])

# Resolver el sistema de ecuaciones Ax = b
x = np.linalg.solve(A, b)

# Mostrar el resultado
print('La cantidad de metros cúbicos que se deben transportar desde cada cantera es:')
for i, val in enumerate(x):
  print(f"Cantera {i+1}: {val:.2f} metros cúbicos")