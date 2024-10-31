import numpy as np


def gaussElim_2v(eq1, eq2):
    m = np.array([eq1, eq2])
    #print(m)

 
    m[0] = m[0] / m[0][0]
   

    m[1] = m[1] - m[0]*m[1][0]

    m[1] = m[1] / m[1][1]
    #print(m)

    m[0] = m[0] - m[1] * m[0][1]
    #print(m)

    return (m[0][2], m[1][2])



if __name__ == '__main__':
    e1 = np.array([15, 2, 6], float)
    e2 = np.array([-5, 2, -4], float)

    sol = gaussElim_2v(e1, e2)

    print("Solution:", sol)