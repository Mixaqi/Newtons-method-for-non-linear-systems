from sympy import diff, symbols
import numpy as np

# Сгенерировать исходную систему, найти вектор-функцию F(X), Матрица Якоби W(x)

amount_of_equations = int(input("Введите число уравнений системы: "))
vector_function = np.arange(amount_of_equations).reshape(3, 4)
print(vector_function)
