import numpy as np
from numpy.linalg import matrix_power

#Checks if an array satisfies probability axiom; Sum of Row = 1
def is_markov( array ):
    indicator = True
    i = 0
    while (i >= 0 and i < len(array) and indicator):
        sum = 0
        for j in range (0, len(array[i])):
            sum += array[i][j]
        if (sum != 1):
            indicator = False
    return indicator


#Reachability: Converts probability matrix to matrix of 1's and 0's. 
#R(i,j) = 1 if P(i, j) > 0, R(i, j) = 0 if P(i, j) = 0. 
def reachable( array ): 
    n = len(array)
    R = np.zeros( (n,n) )
    for i in range(0, n):
        for j in range(0, n):
            if (array[i][j] > 0):
                R[i][j] = 1
    return R

#If i and j communicate, i-> j AND j -> i must be achievable in finite steps; F(i, j) > 0 and F(j, i) > 0
#Finite steps may be narrowed down to paths of max length n-1
#F(i, j) > 0 if S = (I + R^1 + R^2 + ... + R^n-1) > 0, 0 otherwise
#We must have F(i, j) AND F(j, i) > 0, let C = F && F^T (True = 1, False = 0)
#If r and c inhabit the same class, we have C(i, k) = C(j, k)
def comm_class( array ):
    n = len(array)
    result = []
    reach = reachable(array)
    identity = np.identity(n, dtype="float")
    base = np.add(identity, reach)
    F = np.linalg.matrix_power(base,n-1)
    C = np.zeros( (n, n) )
    for i in range (0, n):
        for j in range (0, n):
            if(F[i][j]>0 and F[j][i] > 0):
                C[i][j] = 1
    print(C)
    nodes_covered = {}  #Key: node, Value: # of visits
    for i in range (0, n):  #Initialize hashmap entries to 0.  
        nodes_covered[i] = 0
    
    for r in range (0, n):
        if (nodes_covered[r] == 0):
            com = [r]
            nodes_covered[r] += 1
            for c in range(r+1, n):
                if nodes_covered[c] == 0:
                    if(rowCheck(C, r, c)):
                        com.append(c)
                        nodes_covered[c] += 1
                else: 
                    c += 1
            result.append(com)
        else:
            r += 1
    print(array)
    print(result)
    return result

#Check if rows r and c are identical in matrix X
def rowCheck(X, r, c):
    n = len(X)
    k = 0
    while (k < n):
        if(X[r][k] != X[c][k]):
            return False
        k+=1
    return True

#nxn array with transition probabilities: 0 <= P(col | row) <= 1 
#note, these are zero-indexed test cases. 
my_array1 = np.array([[0, 0, 1.0, 0, 0], 
            [0, 0.50, 0.25, 0.25, 0], 
            [1.0, 0, 0, 0, 0],
            [0, 0, 0, 1.0, 0], 
            [0, 0, 0.333, 0, 0.666]])

my_array2 = np.array([[0.5, 0, 0.5, 0], 
            [0, 0.5, 0, 0.5], 
            [0.5, 0, 0.5, 0], 
            [0, 0.5, 0, 0.5]])

my_array3 = np.array([[1/2, 1/2, 0, 0],
            [1/2, 1/2, 0, 0],
            [1/3, 1/6, 1/6, 1/3], 
            [0, 1, 0, 0]])
    
my_array4 = np.array([[0, 1, 0],
            [0, 0, 1], 
            [1, 0, 0]])

#Communicating states of the chain
comm_class(my_array2)

