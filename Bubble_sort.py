def bubble_sort(a):
    n = len(a)
    for i in range(n):
        swapped = False 

        for i in range(0, n-i-1):
            if a[i-1] > a[i]:
                a[i], a[i-1] = a[i-1], a[i]
                swapped = True
        print(a)

        if swapped == False:
            break

arr = [5,7,2,3,4,9,1,8,0]

bubble_sort(arr)