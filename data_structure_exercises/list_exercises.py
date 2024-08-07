# https://pynative.com/python-list-exercise-with-solutions/

# Exercise 1: Reverse a list in Python
list1 = [100, 200, 300, 400, 500]

list1.reverse()
print(list1)

# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, 
# then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.
# Given:

list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []

for i, j in zip(list1, list2):
    list3.append(i + j)

print(list3)


# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.
# Given:
numbers = [1, 2, 3, 4, 5, 6, 7]

square_list = []

for i in numbers:
    square_list.append(i**2)

print('Squared list: \n', square_list)

# Exercise 4: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []

for i in list1:
    for j in list2:
        list3.append(i + j)

print(list3)


# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. Write a program to iterate both lists simultaneously and 
# display items from list1 in original order and items from list2 in reverse order.
# Given

list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for i, j in zip(list1, list2[::-1]):
    print(i, j)

# Exercise 6: Remove empty strings from the list of strings
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

for i in list1:
    if i == "":
        list1.remove(i) 

print(list1)

res = list(filter(None, list1))
print(res)


# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List
# Given:

list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

# Exercise 8: Extend nested list by adding the sublist
# You have given a nested list. Write a program to extend it by adding the sublist ["h", "i", "j"] in such a way that it will look like the following list.
# Given List:

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# sub list to add
sub_list = ["h", "i", "j"]

final_sub_list = list1[2][1][2] + sub_list

list1[2][1][2].extend(sub_list) 

print(list1)

# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, 
# and if it is present, replace it with 200. Only update the first occurrence of an item.
# Given:

list1 = [5, 10, 15, 20, 25, 50, 20]
list1.index(20) 
list1[list1.index(20)] = 200 
print(list1)

# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.
# Given:

list1 = [5, 20, 15, 20, 25, 50, 20]

for i in list1:
    if i == 20:
        list1.remove(i)

print(list1)