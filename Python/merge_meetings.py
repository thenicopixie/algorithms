"""
Your company built an in-house calendar tool called HiCal. You want to add a feature to see the times in a day when everyone is available.
To do this, you’ll need to know when any team is having a meeting. In HiCal, a meeting is stored as a tuple ↴ of integers (start_time, end_time). These integers represent the number of 30-minute blocks past 9:00am.

For example:

  (2, 3)  # Meeting from 10:00 – 10:30 am
(6, 9)  # Meeting from 12:00 – 1:30 pm

Write a function merge_ranges() that takes a list of multiple meeting time ranges and returns a list of condensed ranges.
For example, given:

  [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
 
your function would return:

  [(0, 1), (3, 8), (9, 12)]
"""

def merge_meetings(meetings):
    meetings.sort()
    i = 0
    while i in range(len(meetings)):
        if len(meetings) == 1:
            break
        if meetings[i+1] and meetings[i][1] >= meetings[i+1][0]:
            if meetings[i][1] >= meetings[i+1][1]:
                meetings[i] = meetings[i]
            else:
                meetings[i] = (meetings[i][0], meetings[i+1][1])
            del(meetings[i+1])
        else:
            i += 1
    return meetings

print(merge_meetings([(0, 1), (3, 5), (4, 8), (9, 10), (10, 12)]))
print(merge_meetings([(1, 2), (2, 3)]))
print(merge_meetings([(1, 5), (2, 3)]))
print(merge_meetings([(1, 10), (2, 6), (3, 5), (7, 9)]))
print(merge_meetings([(1, 3), (2, 4)]))
