""" Insertion Sort
Easy
Company Tags
Implement Insertion Sort and return intermediate states.

Insertion Sort is a simple sorting algorithm that builds the sorted list one element at a time, from left to right. It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

Objective:

Given a list of key-value pairs, sort the list by key using Insertion Sort. Return a list of lists showing the state of the array after each insertion. If two key-value pairs have the same key, maintain their relative order in the sorted list.

Input:

pairs - a list of key-value pairs, where each key-value has an integer key and a string value. (0 <= pairs.length <= 100).
Example 1:

Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]

Output:
[[(5, "apple"), (2, "banana"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")]]
Notice that the output shows the state of the array after each insertion. The last state is the final sorted array. There should be pairs.length states in total.

Example 2:

Input:
pairs = [(3, "cat"), (3, "bird"), (2, "dog")]

Output:
[[(3, "cat"), (3, "bird"), (2, "dog")], 
 [(3, "cat"), (3, "bird"), (2, "dog")],
 [(2, "dog"), (3, "cat"), (3, "bird")]]
In this example, you can observe that the pairs with key=3 ("cat" and "bird") maintain their relative order, illustrating the stability of the Insertion Sort algorithm. """

#In-Place Swapping Mechanism 

def Insertion_sort(pair: list)->list:
    final:list = []
    for i in range(0,len(pair)):
        j:int = i
        while j > 0 and pair[j - 1][0] > pair[j][0]:
            pair[j - 1], pair[j] = pair[j], pair[j - 1]
            j -= 1
        final.append(pair[:])
    return final
        
if __name__ == "__main__":
    pair1 = [(3, "cat"), (3, "bird"), (2, "dog")] 
    pair2 = [(5, "apple"), (2, "banana"), (9, "cherry")]
print(f"Insertion Sort 1: {Insertion_sort(pair1)}")
print(f"Insertion Sort 2: {Insertion_sort(pair2)}")
