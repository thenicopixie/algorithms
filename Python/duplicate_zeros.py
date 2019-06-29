#!/usr/bin/python3

"""
Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.

Do the above modifications to the input array in place, do not return anything from your function.
"""
def duplicateZeros(arr):
    """
    Do not return anything, modify arr in-place instead.
    """
    i = 0
    while i < len(arr)-1:
        if arr[i] == 0:
            arr.insert(i, 0)
            arr.pop()
            i += 1
        i += 1


if __name__ == "__main__":
    a = [1,0,2,3,0,4,5,0]
    print(a)
    duplicateZeros(a)
    print(a)                
