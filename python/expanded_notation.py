'''
Challenge:
Create a function that takes a number and return a string with the number in expanded notation (AKA expanded form).
Examples
expand(13) ➞ "10 + 3"

expand(86) ➞ "80 + 6"

expand(17000000) ➞ "10000000 + 7000000"

expand(5325) ➞ "5000 + 300 + 20 + 5"
'''


def expand(num):
    num = str(num)
    ret = ''
    for i in range(len(num)):
        if int(num[i])>0:
            ret = ret + (' + '+num[i]+('0'*(len(num)-i-1)))
    return ret[3:]