"""
Write a function that takes a list of characters and reverses the letters in place.
"""

def reverse_list_of_characters(l):
    i = 0
    j = len(l)-1
    while i < j:
        temp = l[i]
        l[i] = l[j]
        l[j] = temp
        i += 1
        j -= 1
    return l
        
print(reverse_list_of_characters(["h","e","l","l","o"]))
