# File: homework1. py

# --- 3.1 Variables and Data Types ---
a = 10
b = 1.5
c = 3j
d = "hello"
e = [1, 2, 3]
f = {"name": "Ellen", "favorite fruit": "strawberry"}
g = (1, 2)
h = ["apple", "banana", "strawberry"]
i = True
j = None
k = [True, "blue", 12]
l = str(14)
m = 1e4

# Sorry if this is kinda cheating because we didn't learn loops yet but I didn't want to type print statements for all 13 variables TwT
variables = [a, b, c, d, e, f, g, h, i, j, k, l, m]
for variable in variables:
    print(variable)
    print(type(variable))

"""
a is an integer, a whole number
b is a float, a number that contains a decimal
c is a complex, representing a number on the complex plane
d is a string, a chain of characters
e is a list, a data type that can contain multiple other points of data
f is a dictionary
g is a tuple, which is an immutable list
h is also a list
i is a boolean, a "0 or 1" data type that represents a true or false value
j is a null object and is a placeholder until the variable takes another data type
k is also a list, but one that takes multiple different data types
l is also a string. since 14 is an integer on its own, the str function turns it into a string.
m is equal to 10^4, which is a float.
"""

"""
1. How many different data types did you find?
9

2. List all the data types you found.
integer, float, complex, string, list, dictionary, tuple, boolean, nulltype

3. What variables have the same data types?
e,h,k are all lists
d,l are both strings
b,m are both floats

4. What was the data type of l? Why is it not an integer? What does str() do?
see comment in the previous section under l

5. Look up one more data type not given above. Repeat the same procedure.
"""
n = {"a", "b"}
print(n)
print(type(n))
#n is a set, an unindexed list

# --- 3.2 Booleans ---
booleans = [10 > 9, 10 == 9, 10 <= 9, bool("abc"), bool(123), bool(["apple", "cherry", "banana"]), bool(True), bool(False), bool(0), bool(""), bool(" "), bool(()), bool([]), bool({}), bool(True and False), bool(True and True), bool(False and False), bool(True or False), bool(True or True), bool(False or False), bool(not(False)), bool(not(True))]
for boolean in booleans:
    print(boolean)

"""
True 10 is greater than 9
False 10 is not equal to 9
False 10 is not less than or equal to 9
True a str is a truthy value
True an int is a truthy value
True a list is a truthy value
True True is a truthy value
False False is a falsy value
False 0 is a falsy value
False null is a falsy value
True space is a string an thus is a truthy value
False empty tuple is a falsy value
False empty list is a falsy value
False empty dict is a falsy value
False both statements are not true
True both statements are true 
False both statements are not true
True one of the statements is true
True one of the statements is true
False neither statement is false
True the statement is not false
False the statement is not true
"""

"""
What pattern do you notice about expressions returning True or False?
Stuff that is empty/null/zero tends to be false

Which expression surprised you about its result?
All of them make sense

Create an expression, not given above, that will return True. Why is it True?
boolean(False or (False or True)) - It is true because the nested statement will evaluate true and then the whole expression will evaluate true as well

Create an expression, not given above, that will return False. Why is it False?
boolean(x > y and x < y) - a number cannot be simultaneously larger and smaller than another
"""

# --- 3.3 Operators ---
operations = [10 + 5, 10 - 5, 2 * 4, 6 / 3, 5 % 2, 3 ** 2, 15 // 2, 5 == 2, 10 != 10, 2 < 5, 12 > 5, 5 <= 6, 1 >= 10]
for operation in operations:
    print(operation)

x = 5
x += 5
x -= 4
x *= 3
print(x)

"""
15, + performs addition
5, - performs subtraction
8, * performs multiplication
2.0, / performs division
1, returns the remainder of modular division
9, squares the number
7, returns the result of modular division

False, checks if the two numbers are equal
False, chekcs if the two numbers are not equal
True, checks if a number is less than or equal to another
True, checks if a number is greater than or equal to another

18, the result of the three lines of code are equal to ((5+5)-4)*3
"""

"""
1. What does the operator and do? Write an expression that results in True. Write an expression
that results in False.
It checks whether two statements are simultaenously true
8 - 1 == 7 and 9 + 3 == 12: True
x == 4 and x == 5: False

2. What does the operator or do? Write an expression that results in True. Write an expression
that results in False.
It checks whether at least one of the two statements are true
1 == 2 or 1 == 1: True
7 > 8 or 8 > 9: False

3. What does the operator not do? Write an expression that results in True. Write an expression
that results in False.
It reverses the parity of the expression
not 5 ** 2 > 6 ** 2: True
not 6 ** 2 > 5 ** 2: False
"""

"""
1. What is the difference between / and //?
/ is regular division which can result in a decimal, but // is floor division and will return only the whole portion of the number (modular division)

2. What is the difference between % and //?
% returns the fractional part of the division. In other words, x / y == x // y + x % y

3. What operator would you use to calculate the remainder when dividing two numbers? Give
an example.
%
i.e. 20 % 6 returns 2

4. How do assignment operators work?
An assignment operator, =, assigns the object on the left side of the equals sign to the value of the object on the right side of the equals sign
"""

# --- 3.4 Strings ---
my_string = "hello"
print (my_string) #prints the whole string
print (my_string[0]) #prints the first character of the string
print (my_string[1]) #prints the second character of the string
print (my_string[2]) #prints the third character of the string
print (my_string[3]) #prints the fourth character of the string
print (my_string[4]) #prints the fifth character of the string
print (my_string[-1]) #prints the last character of the string
print (my_string[1:3]) #prints the second to fourth characters of the string
print (my_string[0:5:2]) #prints every second character (indices 0,2,4)
print(len(my_string)) #prints how many characters are in the string
print(my_string + "goodbye") #prints the string with "goodbye" added to the end
print(my_string * 7) #prints the string appended to itself 7 times

"""
1. Define the term slicing. For which of the manipulations did you slice your string?
Slicing is removing parts of the string. The first 9 manipulations all only take a part of the original string.

2. Call the following, describe the result:
name = "Oski"
print("Hello, my name is", name)
It returns the two strings put together

3. Call the following, describe the result.
name = "Oski"
print(f"Hello, my name is {name}")
Same as above

4. What is the difference between the two last print statements?
In the first method, the second item must come directly after the first, but the second method allows one to embed an item within the statement
"""
name = "Oski"
print("Hello, my name is", name)

name = "Oski"
print(f"Hello, my name is {name}")

# --- 3.5 Terminal Commands ---
"""
1. cd
Changes directories and is used to change working folder
cd homework1

2. ls
Lists all files and folders in current working directory
cd python_decal_sp26

3. ls -a
Lists the hidden files and folders, ones starting with dots
cd -a python_decal_sp26

4. mkdir
Creates a folder in the working directory
mkdir new_homework

5. cat
Prints contents of the file into the terminal
cat words.txt

6. pwd
Prints the current working directory
pwd

7. cd ..
Goes up one folder in the path
cd ..

8. cd .
Stays in the same folder
cd .

9. cd ∼
Returns to the home directory
cd ~

10. cp
Copies a file
cp screenshot.png

11. mv
Moves or renames a file
mv old_name.txt new_name.txt

12. rm (be careful with this one)
Shreds/deletes a file permanently
rm old_file.py

13. clear
Clears the terminal screen
clear

14. grep
Searches for an object in the file
grep "hello" homework1.py
"""

"""
1. Look up 3 other commands not present. Define and explain how to use them on the command
line.
head Shows the first 10 lines of a file, useful to glimpse the contents of the file to check it's the right one
head words.txt

tail Is the same thing but the last 10 lines instead
tail words.txt

history Shows the most recent commands
history

2. What is the difference between ls and ls -a?
One lists ordinary files and the other displays the hidden ones

3. What is a hidden file?
A file that starts with a dot in its file name

4. Look up 3 other flags (e.g., -a was a flag for the ls command). Define and explain how to
use them on the command line.
-S sorts by file size
ls -S python_decal_sp26

-R sorts by reverse order
ls -R python_decal_sp26

-t sorts by most recently modified
ls -t python_decal_sp26
"""