#-------------------
#insertion sort
#-------------------

#insertion sort using current value
def insertion_sort(A):
    for i in range(1,len(A)):
        current_number = A[i]
        for j in range(i-1,-1,-1):
            if A[j] > current_number:
                A[j+1] = A[j]
                A[j] = current_number
            else:
                break
                
#insertion sort without current value using for loop               
def insertion_sort1(A):
    for i in range(1,len(A)):
        for j in range(i-1,-1,-1):
            if A[j] > A[j+1]:
                A[j],A[j+1] = A[j+1],A[j]
            else:
                break
#insertion sort using current value using while loop
def insertion_sort2(A):
    for i in range(1,len(A)):
        j = i-1
        while ( A[j]>A[j+1] and  j >= 0):
            A[j],A[j+1] = A[j+1],A[j]
            j-=1
    
    
A = [4,1,6,2,27,3,7,23,16]
print(A)
insertion_sort2(A)
print(A)
