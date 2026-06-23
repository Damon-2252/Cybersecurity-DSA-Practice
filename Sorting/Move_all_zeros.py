"""Move all zeros to end of array:
Given an array of integers arr[], the task is to move all the zeros to the end of the array while
maintaining the relative order of all non-zero elements.

Examples: 
Input: arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: arr[] = [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: arr[] = [10, 20, 30]
Output: arr[] = [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: arr[] = [0, 0]
Output: arr[] = [0, 0]
Explanation: No change in array as there are all 0s."""

#Two-Pointer Method:

def MoveZeros(lst:list)->list:
    i:int = 0
    j:int = 0
    while j < len(lst):
        if lst[j] != 0:
            lst[i],lst[j] = lst[j],lst[i]
            j+=1
            i+=1
        else:
            j+=1
    return lst
    
if __name__ == "__main__":
    lst1:list = [1, 2, 0, 4, 3, 0, 5, 0]
    lst2:list = [10, 20, 30]
    lst3:list = [0, 0]
    print(f"Zero Sorted list1: {MoveZeros(lst1)}")
    print(f"Zero Sorted list2: {MoveZeros(lst2)}")
    print(f"Zero Sorted list3: {MoveZeros(lst3)}")
