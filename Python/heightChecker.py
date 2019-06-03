"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.  (This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)
"""
def heightChecker(self, heights: List[int]) -> int:
  c = 0
  h = sorted(heights)
  for i, v in enumerate(h):
    if v != heights[i]:
      c += 1
  return c

heightChecker([[1,1,4,2,1,3])
heightChecker([7,9,7,6,8,5,4,1,2,3,1,8,9,1,1,7,1,9,2,6,8])
