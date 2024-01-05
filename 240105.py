#split
data = "John,30,Engineer\nAlice,25,Designer\nBob,22,Artist"
lines = data.split("\n")

for line in lines:
    fields = line.split(",")
    print("Name:", fields[0], "Age:", fields[1], "Occupation:", fields[2])

#join
words = ['Hello', 'world', 'this', 'is', 'a', 'test']
sentence = ' '.join(words)
print(sentence)

#split the string
input_str = "Geeks for Geeks"
split_list = input_str.split()
print(split_list)

#join the list of strings
input_list = ['Geeks', 'for', 'Geeks']
joined_str = ' '.join(input_list)
print(joined_str)

#list comprehension
squares = [x**2 for x in range(5) if x%2==0]
print(squares) # [0, 4, 16]

squares = [x**2 for x in range(1,21) if x%3==0]
print(squares) # [9, 36, 81, 144, 225, 324]

squares = [x**2 for x in range(1,6)]
print(squares) # [1, 4, 9, 16, 25]

#enumerate
fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)
enumerate(fruit, start=0)

fruits = ['a', 'b', 'c']

for idx, fruit in enumerate(fruits):
    print(f"fruit{idx} name is {fruit}")

#range를 사용한 코드
for idx in range(len(fruits)):
    print(f"fruit{idx} name is {fruits[idx]}")

#zip
names = ['John', 'Jane', 'Doe']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old.")

name = ["M", "N", "S", "A"]
roll_no = [4, 1, 3, 2]

result = set(zip(name, roll_no))

print(result)

#zip and enumerate
names = ['M', 'R', 'C']
ages = [24, 50, 18]

for idx, (name, age) in enumerate(zip(names, ages)):
    print(f"{idx} {name} {age}")

#lambda
double = lambda x: x * 2
print(double(5)) # 10

#map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x*2, numbers))
print(squared) # [2, 4, 6, 8]
