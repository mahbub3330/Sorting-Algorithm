#-----------------------
#Selection sort
#-----------------------

def selection_sort(A):
    for i in range(0,len(A)-1):
        index = i
        for j in range(i+1,len(A)):
            if (A[index]>A[j]):
                index=j
#         print(index)
        if index!=i:
            A[i],A[index]=A[index],A[i]
A = [4,1,6,2,27,3,7,23,16]
print(A)
selection_sort(A)
print(A)