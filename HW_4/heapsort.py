def pushup(arr,i):
    if arr[i//2]<arr[i]:
        arr[i],arr[i//2]=arr[i//2],arr[i]
        pushup(arr, parent(i))

# Push Down function
def push_down(arr,n,i):
        left= 2 * i + 1
        right=2 * i + 2

        if left >= n:
                return i
        elif right >= n:
                arr[i], arr[left] = arr[left], arr[i]
                return l
        else: 
                if arr[l]>arr[r]:
                        arr[i],arr[left]=arr[left],arr[i]
                        largest=l
                else:
                        arr[i],arr[right]=arr[right],arr[i]
                        largest=r
                return push_down(arr,n,largest)
