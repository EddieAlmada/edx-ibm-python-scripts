# https://pynative.com/python-tuple-exercise-with-solutions/

# Exercise 1: Reverse the tuple
tuple1 = (10, 20, 30, 40, 50)

reversed_tuple = tuple1[::-1]

print("Answer: ", reversed_tuple)

# Exercise 2: Access value 20 from the tuple

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
tuple1[1][1]

# Exercise 3: Create a tuple with single item 50

tuple1= (50, )
print(tuple1)
type(tuple1)

# Exercise 4: Unpack the tuple into 4 variables

tuple1 = (10, 20, 30, 40)

a,b,c,d = tuple1
print(a)
print(b)
print(c)
print(d)


# Exercise 5: Swap two tuples in Python

tuple1 = (11, 22)
tuple2 = (99, 88)

tuple1,tuple2  = tuple2,tuple1

print("Answer: ", tuple1)
print("Answer: ", tuple2)


# Exercise 6: Copy specific elements from one tuple to a new tuple

tuple1 = (11, 22, 33, 44, 55, 66)

tuple2 = tuple1[3:5]
print("Answer: ", tuple2)


# Exercise 7: Modify the tuple

tuple1 = (11, [22, 33], 44, 55)
tuple2 = tuple1[:]
tuple2[1][0] = 222
print("Answer: ", tuple2)


# Exercise 8: Sort a tuple of tuples by 2nd item

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

new_sorted_tuple = tuple(sorted(list(tuple1), key=lambda x: x[1]))

print("Answer: ", new_sorted_tuple)

# Exercise 9: Counts the number of occurrences of item 50 from a tuple

tuple1 = (50, 10, 60, 70, 50)

print("Answer: ", list(tuple1).count(50))

# Exercise 10: Check if all items in the tuple are the same

tuple1 = (45, 45, 45, 45)
validator = 0

for i in tuple1:
    if i == 45:
        validator += 1

if validator == len(tuple1):
    print("All values equal")
else:
    print("Not all values are equal")

all(i == tuple1[0] for i in tuple1)