"""
List Data Type
"""

from typing import List


nums = [21, 12, 10, 6, 2, 42, 0, 31, 13]
names = ['Lorraine', 'Britney', 'Vivian', 'Antoinette']
random = [29, [12, 'twelve'], 'a', 'an', 'a', 'ass', ['Ash', 'Eli', 2019]]

for item in nums : 
    print(nums)

for index in range(len(names)) : 
    print(names[index])

for i, element in enumerate(random) : 
    print(element, "is in position", i)

combine = nums + names 
print(combine)

list_of_zeroes = [0] * 10
print(list_of_zeroes)

empty_list = [None] * 10
print(empty_list)

names.append('Sienna')
vamps = ['Zoey', 'Jesse']
names.extend(vamps)
print(f'Party: {names}')

nums.sort()
print(f'Sorted {nums}')

random.pop(1)
random.remove('a')
del random[1:3]
print(random)

"""
Lists and Functions
"""
print(len(random))
print(sum(nums))
print(min(nums))
print(max(names))

"""
Lists and Strings
"""
my_gf = 'Ashley Diaz'
letters = list(my_gf)
print(letters)

name_format = my_gf.split()
print(name_format)

groceries = 'yogurt-past-boobs-ass'
delimeter = '-'
grocery_list = groceries.split(delimeter)
print(grocery_list)

delimeter = '\n- '
char_list = delimeter.join(names)
print('-', char_list)

"""
Parsing Lines
"""
fhandle = open('mbox.txt') 
for line in fhandle :
    line = line.rstrip()
    if not line.startswith('From '): continue
    line_parts = line.split()
    print(line_parts[2])
    break
fhandle.close()

"""
Objects and Values
"""
a = 'Juice'
b = 'Juice'
print("a and b are the same object:", a is b)

list1 = [19, 23, 2020]
list2 = [19, 23, 2020]
print("list1 and list2 are the same object:", list1 is list2, "\nAre they equivalent?: ", list1 == list2)

"""
Aliasing
"""
characters = ['YunHee', 'JiSu', 'Blake']
eusol = characters
print("characters and eusol are the same object:", characters is eusol)

characters.append('Elisabeth')
print(eusol)

a = 'Orange'
print(a, b)

"""
List Arguments
"""
def delete_head_1 (t: List): 
    del t[0]
    # This changes the aliased object

def delete_head_2 (t: List):
    t = t[1:]
    # This creates a new list altogether

numbers = [2,11,3,7,3,51,21,7,3]
delete_head_1(numbers)
print(numbers)
delete_head_2(numbers)
print(numbers)

numbers_ref = numbers # These two are now referencing the same aliased object
print(f"Are the two array the same? {numbers_ref is numbers}")

numbers_ref.append(47) # Append modifies the list. So this will affect any element referencing the aliased object
print(numbers_ref, numbers, numbers is numbers_ref) 

numbers_ref += [69] # This also modifies the aliased object
print(numbers_ref, numbers, numbers is numbers_ref)

numbers_ref = numbers + [17] # This method creates a new list, so they stop referencing the same object
print(numbers_ref, numbers, numbers is numbers_ref) 

# You can assign the same values of one link to another without aliasing the object by using the copy method
noire = names
print(f"Are noire and names the same? {noire is names}")

noire_char_list = names.copy()
print(f"Are noire_char_list and names the same? {noire_char_list is names}")

la = names[:]
print(f"Are la and names the same? {la is names}")

numbers_ref_2 = numbers.copy()
numbers_ref_2.sort()
print(numbers)

"""
liveCoding
"""
note = 'I love Ashley'
words = note.split()
print(words)

noteWithWhiteSpaces = "There's               different\nsorts of        white\n    spaces"
words_2 = noteWithWhiteSpaces.split()
print(words_2)

noteWIthCol = 'first;second;third'
words_3 = noteWIthCol.split()
print(words_3)
words_4 = noteWIthCol.split(';')
print(words_4)

fhandle = open('mbox-short.txt')
dateArr = [[line.split()[6], line.split()[3], line.split()[4], line.split()[2], line.split()[1].split('@')[0]] for line in fhandle if line.startswith('From ')]
print(dateArr)