import sys, time
from datetime import datetime



def mergeSort(alist):
    if len(alist)<=1:                                           #stopping condition             
        return alist                                            
    mid = len(alist)//2                                         #split list into 2
    lefthalf = alist[:mid]                                      #left half
    righthalf = alist[mid:]                                     #right half
    lefthalf = mergeSort(lefthalf)                              #recurse on left half, get sorted left half
    righthalf = mergeSort(righthalf)                            #recurse on right half, get sorted right half
    return merge(lefthalf, righthalf)                           #merge sorted left and right halves
                

def merge(lefthalf,righthalf):
    merged_list = [0] * (len(lefthalf) + len(righthalf))        
    i=0                                                         #three counters
    j=0
    k=0                                                 
    while i < len(lefthalf) and j < len(righthalf):     
        if lefthalf[i] <= righthalf[j]:                         #if element in left is less than or equal to element in right                                                    
            merged_list[k]=lefthalf[i]                          #add it to the merged list
            i=i+1                                               #move to the next item in the left list
        else:                                                                         
            merged_list[k]=righthalf[j]                         #otherwise move the element in the right list
            j=j+1                                               #to the merged list and move to the next item in the right list
        k=k+1                                                   #move to the next item in the merged list

    while i < len(lefthalf):                                    #if items are left over in the left half,                           
        merged_list[k]=lefthalf[i]                              #add to the merged list
        i=i+1
        k=k+1

    while j < len(righthalf):                                   #if items are left over in the right half,                         
        merged_list[k]=righthalf[j]                             #add to the merged list
        j=j+1
        k=k+1

    return merged_list



def bubble_sort(A):
    
    sort = True       # set the sort variable to true 

    while sort is True:   # while sort is True the loop will run
        sort = False        # we then set the sort to false 
        for i in range(0, len(A)-1): # loop through the len of list a minus 1 
            if A[i] > A[i+1]:       # if the number of this index in list A greater than the number in the next index :
                sort = True         # set the sort to True so that we check the next indexed numebers
                A[i], A[i+1] = A[i+1], A[i] # make the swap so that the greater numnber is on the right
    return A # return sorted list 

def selection_sort(A):
    for i in range(0, len(A)-1):
        min = i
        for j in range(i + 1, len(A)):
            if A[j] < A[min]:
                min = j
        if min != i:
            A[i], A[min] = A[min], A[i]
    return A


def quickSort(A):
    
    
    L = []
    G = []
    
    if len(A) <= 1:
        return A
    else:
        pivot= A[len(A)//2]
    
    for x in A:
        if x <= pivot:
            L.append(x)
        else:
            G.append(x)

        
    return L + G

def insertionSort(A):
    
    for i in range(1, len(A)):
        key = A[i]
        j = i 
        while j >= 0 and A[j-1]> key:
                A[j] = A[j-1]
                j -= 1
        A[j] = key
    return A



Hundred_list = [8, 32, 18, 53, 21, 23, 3, 81, 38, 14, 61, 7, 56, 31, 50, 44, 16, 17, 42, 57, 95, 55, 100, 78, 9, 68, 24, 75, 69, 96, 28, 84, 82, 2, 36, 94, 80, 15, 39, 99, 43, 25, 10, 87, 63, 41, 72, 65, 35, 12, 60, 33, 79, 90, 5, 51, 54, 74, 37, 40, 11, 93, 59, 98, 27, 49, 89, 83, 77, 86, 91, 97, 46, 1, 6, 76, 45, 73, 52, 88, 70, 13, 47, 85, 4, 34, 22, 20, 92, 62, 19, 64, 71, 66, 30, 26, 29, 58, 48, 67]

def main():
    
    for i in range(1):                                           #decide a range
                                                                 #print the result once only
                            
                                                                #print the time taken too
    
        
        for i in range(1): 
            start = datetime.now()
            res = mergeSort(Hundred_list)   
            print('\n')
            print(f'Merge: {res}')                                         
            delta = datetime.now() - start
            print( 'Merge Time : %fs' % \
                delta.total_seconds())                                      
        
        for i in range(1): 
            start = datetime.now()
            bub_sort = bubble_sort(Hundred_list)
            print('\n')
            print(f' bubble: {bub_sort}')
            delta = datetime.now() - start
            print( 'Bubble Time : %fs' % \
                    delta.total_seconds())  

        for i in range(1):  
            start = datetime.now()
            sel = selection_sort(Hundred_list)  
            print('\n')
            print(f'selection : {sel} ')
            delta = datetime.now() - start
            print( 'Selection Time : %fs' % \
                    delta.total_seconds()) 

        for i in range(1): 
            start = datetime.now()
            quick = quickSort(Hundred_list) 
            print('\n')
            print(f'Quicksort:{quick}')
            delta = datetime.now() - start
            print( 'Quicksort Time : %fs' % \
                    delta.total_seconds())

        for i in range(1):
            start = datetime.now()
            insert = insertionSort(Hundred_list)
            print('\n')
            print(f'Inerstion Sort :{insert}') 
            delta = datetime.now() - start
            print( 'Inerstion Sort Time : %fs' % \
                    delta.total_seconds()) 
        

if __name__ == '__main__':
    sys.exit(main())

    
