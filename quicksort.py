def Quicksort(arr):
    if len(arr)<2:
        return arr
    else:
        pivo = arr[0]
        menores = [i for i in arr[1:] if i <= pivo]
        maiores = [i for i in arr[1:] if i > pivo]
        return Quicksort(menores) + [pivo] + Quicksort(maiores)

print(Quicksort([10,5,2,25,64,78,54,3,74,88]))