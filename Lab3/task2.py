def zeros(lst):
    count = 0
    for num in lst:
        if num == 0:
            count = count + 1
    return count 


z=zeros([0,1,2,3,4,5])

print(z)