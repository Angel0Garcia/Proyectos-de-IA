def Grades(a):
    m = len(a)
    FinalGrades = []

    for i in range (0, m):
        if a[i] >= 60 and a[i] <= 69:
            FinalGrades.append('D')
        elif a[i] >= 70 and a[i] <= 79:
            FinalGrades.append('C')
        elif a[i] >= 80 and a[i] <= 89:
            FinalGrades.append('B')
        elif a[i] >= 90 and a[i] <= 100:
            FinalGrades.append('A')
        else:
            FinalGrades.append("failed")

    print(FinalGrades)
            

arr = [75,93,62,69,78,93,58]

Grades(arr)