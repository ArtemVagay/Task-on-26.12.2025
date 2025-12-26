# 1 и 2(1)
lst1 = [1,4,5,4,3,5,2,4,2,4,3]

def find_max_element(biggest, count, lst):
    max_element = 0
    if count < biggest:
        for i in range(len(lst)):
            if max_element < lst[i]:
                   max_element = lst[i]
        if count + 1 == biggest:
            print(lst.index(max_element) + 1)
        lst.remove(max_element)
        return find_max_element(biggest, count+1, lst)
lst = list(lst1)
find_max_element(2, 0, lst)
lst = list(lst1)
find_max_element(3, 0, lst)
# 3(1)
lst1 = [1,4,5,4,3,5,2,4,2,4,3]
count = 0
for i in range(1, len(lst1) - 1):
    if lst1[i - 1] < lst1[i] > lst1[i + 1]:
        count += 1
print(count)
# 2
lst1 = [4, 8, 12, 14, 23, 85]
lst2 = [2, 4, 8, 9, 12, 16]
lst = lst1 + lst2
print(lst)
for i in range(len(lst) - 1):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)
# 1(3) 1 Вариант
lst = [1,4,5,4,3,5,2,4,2,4,3]
for i in range(len(lst) - 1):
    if lst[i] + lst[i+1] % 2 != 0:
        print(f"{lst[i]} и {lst[i+1]}")
# 1 (3) 2 Вариант
lst = [1,4,5,4,3,5,2,4,2,4,3]
for i in range(len(lst) - 1):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
print(lst)
for i in range(len(lst) - 1):
    if lst[i] + lst[i+1] % 2 != 0:
        print(f"{lst[i]} и {lst[i+1]}")
# 2 (3) 1 Вариант
lst = [1,4,5,4,3,5,2,4,2,4,3]
count = 0
for i in range(len(lst)):
    firstness = True
    for j in range(len(lst)):
        if lst[i] == lst[j] and i != j:
            firstness = False
    if firstness:
        count += 1
print(count)
# 2 (3) 2 Вариант
lst = [1,4,5,4,3,5,2,4,2,4,3]
for i in range(len(lst) - 1):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
count = 0
for i in range(len(lst)):
    firstness = True
    for j in range(len(lst)):
        if lst[i] == lst[j] and i != j:
            firstness = False
    if firstness:
        count += 1
print(count)
# 3 (3) 
lst = [1,4,5,4,3,5,2,4,2,4,3]
for i in range(len(lst) - 1):
    for j in range(len(lst) - i - 1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]

length_lst = []
for i in range(len(lst) - 1):
    length = 0
    for j in range(i, len(lst) - 1):
        if lst[j] + 1 == lst[j + 1]:
            length += 1
    length_lst.append(length)
print(length_lst) 