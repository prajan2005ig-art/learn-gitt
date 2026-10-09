def reversal(arr,start,end):

    if start >= end:
        return arr

    arr[start],arr[end] = arr[end],arr[start]
    return reversal(arr,start+1,end-1)

arr = [1,2,3,4,5,6,7,8,9]
result = reversal(arr,0,len(arr)-1)
print(result)