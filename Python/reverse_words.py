"""
Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place.
"""
def reverse_words(l):
    reverse_string(l, 0, len(l)-1)
    x = 0
    for i in range(len(l)+1):
        if (i == len(l)) or (l[i] == ' '):
            reverse_string(l, x, i - 1)
            x = i + 1
    return l

def reverse_string(s, i, j):
    while i < j:
        temp = s[i]
        s[i] = s[j]
        s[j] = temp
        i += 1
        j -= 1
    return s
    
print(reverse_words([ 'c', 'a', 'k', 'e', ' ', 'p', 'o', 'u', 'n', 'd', ' ', 's', 't', 'e', 'a', 'l' ]))
