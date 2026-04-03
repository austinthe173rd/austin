#3.1
def say_goodbye():
    print("Goodbye!")

#3.2
def circle_area(radius):
    pi = 3.14
    area = pi * radius**2
    print(area)

#4.1
def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

#5.1
def max_min_temps(temperatures):
    min_max = (min(temperatures), max(temperatures))
    print (min_max)

#5.2
def is_weekend(day_index):
    weekends = [6, 7]
    if day_index in weekends == true:
        return True
    else:
        return False

#5.3
def fuel_efficiency(distance, fuel):
    return distance / fuel

#5.4
def encrypt(integer):
    encrypted_integer = (integer % 10) * 10**(len(str(abs(integer))) - 1) + integer // 10
    return int(encrypted_integer)

#6.1
def power(x, y):
    for _ in range(y):
        x *= x
    return x

#6.2.1
def maximum_for(list):
    maximum_value = list[0]
    for item in list:
        if item > maximum_value:
            maximum_value = item
    return maximum_value

def minimum_for(list):
    minimum_value = list[0]
    for item in list:
        if item < minimum_value:
            minimum_value = item
    return minimum_value

#6.2.2
def maximum_while(list):
    index = 0
    minimum = list[0]
    while index < len(list):
        if list[index] < minimum:
            minimum = list[index]
        index += 1
    return minimum

def minimum_while(list):
    index = 0
    maximum = list[0]
    while index < len(list):
        if list[index] > maximum:
            maximum = list[index]
        index += 1
    return maximum

#6.3
def digit_sum(integer):
    int_str = str(integer)
    int_list = list(int_str)
    int_list2 = [int(a) for a in int_list]
    return sum(int_list2)

integer = 1234
result = digit_sum(integer)
print(f"The result of Digit Sum (6.3) with integer = {integer} is {result}")