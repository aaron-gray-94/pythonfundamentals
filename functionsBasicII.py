def countdown(a):	# function name: 'add', parameters: a and b
    x=[]
    for i in range(a,-1,-1):
        x.append(i)
    return x
x=countdown(5)
print(x)

def printvals(arr):
    for val in arr:
        print(val)
printvals([3,5])

def firstpluslen(arr):
    x=arr[0]+arr[len(arr)-1]
    return x
x=firstpluslen([1,2,3])
print(x)

def valsgreatersecond(arr):
    x=[]
    if len(arr)<3:
        return "Error"
    else:
        second=arr[2]
        for v in arr:
            if v>=second:
                x.append(v)
        return x
x=valsgreatersecond([5,2,3,2,1,4])
print(x)
x=valsgreatersecond([1,2])
print(x)

def len_and_value(length,value):
    x=[]
    for i in range(0,length,1):
        x.append(value)
    return x
x=len_and_value(4,7)
print(x)