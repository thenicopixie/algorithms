# Increment an arbitrary-precision integer
# Write a program that takes as an input an array of digits encoding
# a nonnegative decimal integer and updates the 
# array to represent the integer D + 1
# example: [1,2,9] => [1,3,0]

# brute force solution

def plus_one(A):
        """A: an array of intgers
           Return: Array incremented by one
        """
        A[-1] += 1
        for i in reversed(range(1, len(A))):
            if A[i] != 10:
                break
            A[i] = 0
            A[i - 1] += 1
        if A[0] == 10:
            A[0] = 1
            A.append(0)
        return A

print(plus_one([1,2,9]) == [1,3,0])
print(plus_one([2,9,9]) == [3,0,0])
