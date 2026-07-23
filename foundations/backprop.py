import numpy as np
from numpy.typing import NDArray
from typing import Tuple


class Solution:
    def backward(self, x: NDArray[np.float64], w: NDArray[np.float64], b: float, y_true: float) -> Tuple[NDArray[np.float64], float]:
        # x: 1D input array
        # w: 1D weight array
        # b: scalar bias
        # y_true: true target value
        #
        # Forward: z = dot(x, w) + b, y_hat = sigmoid(z)
        # Loss: L = 0.5 * (y_hat - y_true)^2
        # Return: (dL_dw rounded to 5 decimals, dL_db rounded to 5 decimals)
        z = np.dot(w,x) + b
        y_activate = 1.0 / (1.0 + math.exp(-z))
        dL_dz = (y_activate - y_true) * y_activate * (1.0 - y_activate)
        dL_dw = np.empty_like(x)
        np.multiply(x,dL_dz, out=dL_dw)
        np.round(dL_dw,5,out=dL_dw)
        dL_db = round(dL_dz, 5)
        return dL_dw,dL_db
