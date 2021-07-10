def biggie_size(arr):
    for i in range(0,len(arr),1):
        if arr[i] > 0:
            arr[i] = "big"
    return arr
print(biggie_size([-1,3,5,-5]))

def count_positives(arr):
    count=0
    for i in range(0,len(arr),1):
        if arr[i] > 0:
            count=count+1
    arr[len(arr)-1]=count
    return arr
print(count_positives([1,6,-4,-2,-7,-2]))

def sum_total(arr):
    sum=0
    for val in arr:
        sum=sum+val
    return sum
print(sum_total([1,2,3,4]))

def average(arr):
    sum=0
    for val in arr:
        sum=sum+val
    avg=sum/len(arr)
    return avg
print(average([1,2,3,4]))

def length(arr):
    return len(arr)
print(length([37,2,1,-9]))

def minimum(arr):
    if len(arr)==0:
        return "Error"
    else:
        min=arr[0]
        for val in arr:
            if val<min:
                min=val
        return min
print(minimum([2,5,0]))

def maximum(arr):
    if len(arr)==0:
        return "Error"
    else:
        max=arr[0]
        for val in arr:
            if val>max:
                max=val
        return max
print(maximum([2,10,3]))

def ultimate_analysis(arr):
    sum=0
    min=arr[0]
    max=arr[0]
    for val in arr:
        if val>max:
            max=val
        if val<min:
            min=val
        sum=sum+val
    average=sum/len(arr)
    length=len(arr)
    return {'sumTotal':sum, 'average':average, 'minimum':min, 'maximum':max, 'length':length}
print(ultimate_analysis([37,2,1,-9]))

def reverse_list(arr):
    for i in range(0,round(len(arr)/2),1):
        temp=arr[i]
        arr[i]=arr[len(arr)-i-1]
        arr[len(arr)-i-1]=temp
    return arr
print(reverse_list([37,2,1,-9,2]))