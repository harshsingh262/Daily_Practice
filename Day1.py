def bubbleSort(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
arr=[100,85,45,9,250,-8,6]
bubbleSort(arr)
print(arr)