def linearSearch(arr,x):
    n=len(arr)
    for i in range(n):
        if arr[i]==x:
            return 1
    return -1
arr=[1,2,3,4,40,10]
x=int(input("Enter the number"))
result = linearSearch(arr,x)
if result != -1:
    print("Element is present in array")
else:
    print("Element is not present in array")