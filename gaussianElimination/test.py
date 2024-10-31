import numpy as np
from gauss import gaussElim_2v

eq1 = np.array([15, 2, 6], float)
eq2 = np.array([-5, 2, -4], float)

sol = gaussElim_2v(eq1, eq2)

print("Solution:", sol)