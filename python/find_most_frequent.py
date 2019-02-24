'''
Challenge:
Create a function that takes a list and return the most frequently occurring element contained within it.

Examples
find_frequent([3, 7, 3]) ➞ 3

find_frequent([None, "hello", True, None]) ➞ None

find_frequent([False, "up", "down", "left", "right", True, False]) ➞ False
'''


def find_frequent(lst):
	vals = {}
	for elm in lst:
		if elm not in vals:
			vals[elm] = 1
		else:
			vals[elm] +=1
	return max(vals, key = vals.get)

