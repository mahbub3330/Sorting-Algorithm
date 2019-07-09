#-------------------
#Bubble sort
#-------------------

def bubble_sort(A):
    for i in range(len(A)-1,0,-1):
        for j in range(i):
            if A[j]>A[j+1]:
                A[j+1],A[j]=A[j],A[j+1]
A=[7,4,2,5,12,1,3]
bubble_sort(A)
print(A)