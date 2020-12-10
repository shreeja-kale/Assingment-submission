#Question 1
#Try 5 Different functions of the String in Python.
#1
str = 'Python is cool'
print(str.split())
#2
string = "Shreeja Kale"
print(string.upper())
#3
language = {'Python', 'Java', 'Ruby'}
s = '->'
print(s.join(language))
#4
city = "I AM FROM INDORE"
print(city.lower())
#5
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
index = vowels.index('o')
print('The index of o:', index)
print('Question 1 ended')
print('Question 2 starts')
#Question 2
#Try 5 Different functions of the List object in Python
#1
names = ['reetu', 'payal', 'riya', 'sneha']
names.insert(3, 'neeti')
print('Updated List:', names)
#2
num = ['1', '2', '3', '4']
num.remove('3')
print('Updated animals list: ', num)
#3
OS = ['linux', 'windows', 'ubuntu']
print('Original List:', OS)
OS.reverse()
print('Updated List:', OS)
#4
my_items = ['sugar', 0, 'salt']
new_items = my_items.copy()
print('Copied List:', new_items)
#5
list = [{1, 2, 3}, ('priya')]
list.clear()
print('List:', list)
print('Question 2 ended')
print('Question 3 starts')
#Question 3
#Experiment with at least 5 default functions of Dictionary
#1
sales = { 'apple': 1, 'orange': 2, 'grapes': 3 }
print(sales.items())
#2
sales = { 'apple': 1, 'orange': 2, 'grapes': 3 }
print(sales.values())
#3
d = {'x': 2}
d.update(y = 4, z = 5)
print(d)
#4
girl = {'name': 'divya', 'age': 20, 'salary': 10000}
print(girl.keys())
empty_dict = {}
print(empty_dict.keys())
#5
girl = {'name': 'shreya', 'age': 24}
age = girl.setdefault('age')
print('person = ',girl)
print('Age = ',age)
print('Question 3 ends')