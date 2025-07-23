"""fahrenheit = input("Please type a temperature in Fahrenheit: ")
fahrenheit = int(fahrenheit)
celsius = (fahrenheit - 32) * 5 / 9
celsius = round(celsius, 2)
print("This temperature in Celsius is", celsius)"""

"""a = input("Enter a value for ‘a’: ")
b = input("Enter a value for ‘b’: ")
a = float(a)
b = float(b)
sum = a + b
product = a * b
print("The value 'a' was", a, "and the value 'b' was", b)
print("The sum of 'a' and 'b' is", sum)
print("The product of 'a' and 'b' is", product)"""

"""num_1 = input("Please input number 1: ")
num_2 = input("Please input number 2: ")
num_3 = input("Please input number 3: ")
num_1 = float(num_1)
num_2 = float(num_2)
num_3 = float(num_3)
list = [num_1, num_2, num_3]
print("The largest number you imputed is", max(list))"""

"""name = "Black Knight"
print(name[0])
print(name[4])
print(name[-1])
print(name[-2])
print(name[2:5])
print(name[6:])
print(name[:5])
print(name[:])"""

names = ["Terry", "John", "Michael", "Eric", "Terry", "Graham"]
"""print(names[2])
print(names[-2])
print(names[0:3])"""

names = names + ["Brian"]

names[0:1] = ["Mark", "Jon"]
print(names)
