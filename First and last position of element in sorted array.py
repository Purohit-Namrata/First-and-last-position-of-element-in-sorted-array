def first_and_last(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            start=i
            while i+1 < len(arr) and arr[i+1] == target:
                i=i+1
            return [start,i]
    return [-1,-1]

index=first_and_last([5, 7, 7, 8, 8, 10],8)
print("First and last position of element in sorted array: ",index)
