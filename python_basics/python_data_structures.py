# Tuples
## Ordered sequence

tuple_1 = ('eddie', 13, 3.4, 'hi')
tuple_1[0]

tuple_2 = tuple_1 + (3, 'python')
tuple_2
type(tuple_2)
tuple_2[1:3]
len(tuple_2)

ratings = (10,9,6,5,10,8,9,6,2)
sorted(ratings)

tuple_3 = tuple_2 + ((2,3,4), 'r')
tuple_3[6][2]

# List
# Lists are also ordered sequences
# Here is a List "L"
# A list is represented with square brackets
# List are mutable

L = ['Michalel Jackson', 10,1, 1982, "MJ", 1]
type(L)

L[1]
L[-1]

L[3:5]

L1 = L+["pop", 18]
L
## Adds two elements
L.extend(["pop",10])
# Adds one element
L.append(["rock",45])

del(L[-1])
L

L2 = L[:]
L2[1] = 'hi'
L2
L3 = L2.copy()

L3.count(1)


my_list = [1, 2, 3, 4, 5] 
my_list.insert(2, 6) 
print(my_list)

my_list.pop(2)


my_list = [1, 2, 3, 4, 5] 
my_list.reverse() 
print(my_list) 
my_list.sort() 

# Dictionariee
# keys and values
# Doneted by curly brackets

dict_name = {} #Creates an empty dictionary
person = { "name": "John",  "age": 30, "city": "New York"}

name = person["name"]
age = person["age"]

person.values()
person.update({"Profession": "Doctor"})

person

if "name" in person:
    print("Name exists in the dictionary.")

person_values = list(person.values()); person_values

info = list(person.items()); info


# Sets
# Type of collectios
# Unordered
# Unique values

my_list = [1, 2, 3, 4, 5,2,4,5,2] 
my_list
my_set = set(my_list)
my_set

my_set.remove(1)

2 in my_set


