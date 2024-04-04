def fat(x):
    if x == 1:
        return x
    else:
        return x*fat(x-1)
    
print(fat(3))