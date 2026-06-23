"""Sort a Binary Array
Given an array of 0s and 1s in random order. Segregate 0s on left side and 1s on right side of the array.

Examples: 

Input :  arr[] = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0] 
Output : arr[] = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1] 

Input :  arr[] = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1] 
Output : arr[] = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]"""

# Two-Pointer Method:
def Sortl(lst)-> list:
    i:int = 0
    j:int = len(lst) - 1
    while i <= j:
        if lst[i] == 1 and lst[j] == 0:
            lst[i],lst[j] = lst[j],lst[i]
            i+=1
            j-=1
        elif lst[i] == 0:
            i+=1
        elif lst[j] == 1:
            j-=1
    return lst

if __name__ == "__main__":
    lst:list = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    print(f"Sorted List: {Sortl(lst)}")
