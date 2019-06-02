"""
Given an array sort in place so that A[0] <= A[1] >= A[2] <= A[3] ...
"""
def alternating_array(A):
    i = 0
    A.sort()
    for i in range(len(A)):
        if i % 2 != 0:
            if A[i] <= A[i-1] or A[i] <= A[i+1]:
                temp = A[i + 1]
                A[i + 1] = A[i]
                A[i] = temp
        i += 1
    return A
                
                
print(alternating_array([1,2,3,4,5,6,7,8,9]))
print(alternating_array([5,6,7,8,9,10,11]))
print(alternating_array([5,3,8,9,2,1,4]))
