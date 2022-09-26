print("Hello!")

#задание 2 

a = int(input('input a number:'))
b = int(input('input another number:'))
if a < b :
    print(f'{a} меньше {b}')

else: 
    print(f'{b} меньше {a}')



#задание 3

X = int(input('Enter number A:'))
y = int(input('Enter number B:'))
Z = int(input('Enter number C:'))

#function to get the greatest number from input

def greatest_number (a,b,c):
    maximum_ = max(a,b,c)
    print(f'{maximum_} найбольшее число')
if X == y == Z:
    print('числа равны')
else: 
    func_ = greatest_number(X,y,Z)
    
    
#задание 4

X = int(input('Enter number A:'))
y = int(input('Enter number B:'))
Z = int(input('Enter number C:'))

LIST = [X,y,Z]
unique_LIST = []
# creat LIST of unique elements
for j in LIST:
    if j not in unique_LIST:
        unique_LIST.append(j)
print('есть', len(unique_LIST), 'уникальные числа')



    



