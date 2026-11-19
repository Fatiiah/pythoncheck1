def find_largest(a, b, c):
    maximum = max(a, b, c)
    return maximum  
print(find_largest(2,3,5))

def reverse_string(string):
    return string[::-1]
print(reverse_string("hello there"))

def count_vowels(string):
    count = 0
    vowels = "aeiou"
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count
print(count_vowels("hello thEre"))

def averag(numbers):
    return sum(numbers)/ len(numbers)

print(averag([1,2,3,4]))

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

print(is_palindrome("racECar"))

def remove_duplicates(strings):
    dupl = list(set(strings))
    return dupl

print(remove_duplicates("trripssss"))

def calculate_grade(score):
    if score >= 70:
        return "A"
    elif score >= 60:
        return "B"
    elif score >= 50:
        return "C"
    elif score >= 45:
        return "D"
    elif score >= 40:
        return "E"
    else:
        return "F"     

print(calculate_grade(45))

def sum_list(numbers):
    return sum(numbers)

print(sum_list([1,2,3,4,5]))

def find_min_max(number):
    output = []
    largest = max(number)
    minimum = min(number)

    output.append(largest)
    output.append(minimum)
    return output
print(find_min_max([1,2,3,4,5]))

def separate_number(numbers):
    even = []
    odd = []

    for num in numbers:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
    return even, odd

print(separate_number([1,2,3,4,5,6,7,8,9]))


def merge_lists(list1, list2):
    return list1 + list2

print(merge_lists([1, 2, 3], [4, 5, 6]))


def calculate_total(my_dict):
    return sum(my_dict.values())

prices = {
    'apple': 100,
    'banana': 50,
    'orange': 150,
    'mango': 200
}

print(calculate_total(prices))


