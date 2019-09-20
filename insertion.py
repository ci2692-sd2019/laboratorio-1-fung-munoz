def insertion_sort(A, array_size:int):    

    for i in range (1, len(A)):                 
        x = int(A[i])
        y = i - 1

        while y >= 0 and x < int(A[y]):
            A[y+1] = A[y]
            y = y - 1
        
        A[y+1] = x
    
    for j in range (0, len (A)):
        print (' | ', int(A[j]), end = '')
    