import math

def binary_search(A,T):
    L = 0
    R = len(A) - 1

    while L <= R:
        m = math.trunc((L + R) / 2)
        if A[m] < T:
            L = m + 1
        elif A[m] > T:
            R = m - 1
        else:
            print(m)
            break
    return print("unsuccesful")
    
arr = [1,2,3,4,5,6,7,8,9]

binary_search(arr,10)

