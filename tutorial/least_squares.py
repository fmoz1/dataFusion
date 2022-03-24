#!/usr/local/bin/python
# -*- coding: utf-8 -*-
# udemy/dynamic_systems/least_squares_estimation

import numpy as np
from torch import inverse
# estimation of a vector constant
# y is an array of temperature
# y: 5 x 1
y = np.matrix([[65, 65, 81, 92, 97]]).T
# H: 5 x2
H = np.matrix([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]])

# (H^T H)
H.T * H

# inverse of (H^T H)^{-1}
(H.T * H).I

# inverse multiplied by H^T
(H.T * H).I * H.T

# obtain estimated x
x_hat = (H.T * H).I * H.T * y

# matrix([[ 9.1],
#         [52.7]])
# so, line of best fit
# t = 9.1 * r + 52.7


import numpy as np

def CalculateLeastSquaresSolution(Hmatrix,Ymatrix):
  # Enter Y our Code Here to calculate the least Squares Solution
  Xmatrix = (Hmatrix.T * Hmatrix).I * Hmatrix.T * Ymatrix
  return Xmatrix


y = np.matrix([[65, 65, 81, 92, 97]]).T
# H: 5 x2
H = np.matrix([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]])

LineParam = CalculateLeastSquaresSolution(H, y) 
print(LineParam) 
