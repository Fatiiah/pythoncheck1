#question 1
my_list = [2, 3, 6]

result = 1

for num in my_list:
    result *= num

print("Result =", result)

#question 2
my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

my_list.sort(key=lambda x: x[-1])

print(my_list)

#question 3
d1 = {'a': 100, 'b': 200, 'c': 300}

d2 = {'a': 300, 'b': 200, 'd': 400}

for i in d1.keys():
    if i in d2:
        d1[i] += d2[i] 

print(d1)

#question 4
n = int(input("Enter a number: "))

squares = {}

for i in range(1, n + 1):
    squares[i] = i * i

print(squares)

#question 5
my_list = [
    ('item1', '12.20'),
    ('item2', '15.10'),
    ('item3', '24.5')
]

my_list.sort(key=lambda x: float(x[1]), reverse=True)

print(my_list)

#question 6
my_set = {0, 1, 2, 3, 4}

for item in my_set:
    print(item)

my_set.add(5)
print(my_set)

my_set.remove(2)
print(my_set)
