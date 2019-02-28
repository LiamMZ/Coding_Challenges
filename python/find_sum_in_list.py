'''
Challenge:
Given a number and a list of numbers find if two members of the list add up to the number
return 1 if such a pair is found
return 0 otherwise
'''


def isSumPossible(a, N):
    a = list(a)
    a.sort()
    l = 0 
    r = len(a)-1
    while(l<r):
        if(a[l]+a[r]==N):
            return 1
        elif(a[l]+a[r]<N):
            l+=1
        else:
            r-=1
    return 0


test1 = [11,18,21,28,31,38,40,55,60,62]
test2 = [18,11,21,28,31,38,40,55,60,62]

print(isSumPossible(test2, 66))

