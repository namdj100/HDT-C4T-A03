'''
loop = True
count = 0
while loop:
    print('Hi')
    count += 1
    if count == 3:
        loop = False
        print('done')
'''
'''
b = [4,5,1,8,9,10,5,6,4,3]
print (b[0:3])
print (b[-3:])
b.sort()
print(b)
b.sort(reverse=True)
print(b)
'''
'''
a = [1,4,3,13,9,8]
sort = True
while True:
    sort = False
    for num in range(len(a)-1):
        if a[num] > a[num+1]:
            a[num], a[num+1] = a[num+1], a[num]
            sort = True

print(a)
'''
# list1 = [1,3,4,16,32,8,64,4,128,2,256,32]
# list2 = [16, 2, 4, 2, 128, 64, 16, 7, 1, 64, 32, 16, 5, 8]
# for count,num in enumerate(list1):
#     print(count,num)


# Bài tập về nhà
while True:
    n = int(input())
    for i in range(2, n):
        if n % i == 0:
            print('Đây là hợp số')
        elif n == 9:
            print('Đây là hợp số')
#bất lực với số 9:(((
        else:
            print('Đây là số nguyên tố')
        break        
        
