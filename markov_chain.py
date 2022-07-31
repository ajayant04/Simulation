import numpy as np

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

def comm_class( array ): #Excludes self-communicating classes
    n = len(array)
    result = []
    for i in range (0, n):
        com = [i+1]
        for j in range (i, n):
            if array[i][j] * array[j][i] > 0:
                com.append(j+1)
        
        if len(com) < 2: #No connected node
            continue
        if len(com) == 2 and com[0] == com[1]: #only self communicating
            continue
        elif (com[0] == com[1]): #self-communicating with other elements
            com = com[1:]
            result.append(com)
        else:
            result.append(com)
    return result
        
def print2D (array):
    for i in range (0, len(array)):
        print("[", end = " ")
        for j in range (0, len(array[i])):
            print(str(array[i][j]), end = " ")
        print("]", end = " ")
        print()
    
    return











#nxn array with transition probabilities, state (row) to (column)

my_array1 = [[0.25, 0.25, 0.5, 0, 0], 
            [0, 0.66, 0, 0.33, 0], 
            [0, 0.25, 0.25, 0.25, 0.25],
            [0.5, 0, 0, 0.25, 0.25], 
            [0, 0, 0, 0.2, 0.8]]

my_array2 = [[0.5, 0, 0.5, 0], 
            [0, 0.5, 0, 0.5], 
            [0.5, 0, 0.5, 0], 
            [0, 0.5, 0, 0.5]]

my_array3 = [[1/2, 1/2, 0, 0],
            [1/2, 1/2, 0, 0],
            [1/3, 1/6, 1/6, 1/3], 
            [0, 1, 0, 0]]

#Communicating states of the chain


classes = comm_class(my_array3)
print(classes)
