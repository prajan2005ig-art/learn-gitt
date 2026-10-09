def stack(arr,index):
    if index == len(arr):
        return 0

    return arr[index] + stack(arr,index+1)

arr = [1,2,3,4,5,6,7,8,9]

print(stack(arr,0   ))
