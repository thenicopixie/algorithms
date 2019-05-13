"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        i = 1
        while i <= n:
            if i % 15 == 0:
                l.append("FizzBuzz")
            elif i % 3 == 0:
                l.append("Fizz")
            elif i % 5 == 0:
                l.append("Buzz")
            else:
                l.append(str(i))
            i += 1
        return l
