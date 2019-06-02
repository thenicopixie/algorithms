"""
Given a list of coordinates and a number return a list of k nearest coordinates closest to the origin (0,0)
"""
import math
def findDistance(v):
    return math.sqrt(math.pow(1, 2) + math.pow(2, 2))

def findNearestCoordinates(values, number):
    values.sort(key=findDistance)
    return values[:number]


coordinates = [(1, 2), (3, 4), (4, 7), (6, 7)]
number = 2
print(findNearestCoordinates(coordinates, number))
