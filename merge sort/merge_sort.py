#----------------
# merge sort
#----------------

def merge_sort(A,first_index,last_index):
    if first_index<last_index:
        middle_index = (first_index + last_index )//2  
        
        merge_sort(A,first_index,middle_index) 
        merge_sort(A,middle_index+1,last_index)
        
        merge(A,first_index,middle_index,last_index)

def merge(A,first_index,middle_index,last_index):
    
    Left = A[first_index:middle_index+1]
    Right = A[middle_index+1:last_index+1]
    
    Left.append(999999)
    Right.append(999999)
    
    i = j = 0
    
    for c in range(first_index,last_index+1):
        if Left[i]<= Right[j]:
            A[c] = Left[i]
            i += 1
        else:
            A[c] = Right[j]
            j += 1
            
            
number= int(input("Enter number of element for making your list: "))
list1 = [int(input()) for x in range(number)]

merge_sort(list1,0,len(list1)-1)
list1 