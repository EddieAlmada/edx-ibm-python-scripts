# Exercise 1: Create a list by picking an odd-index items from the first list and even index items from the second
# Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.
# Given:

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]

odd_elements = l1[1::2]
print("Element at odd-index positions from list one")
print(odd_elements)

even_elements = l2[0::2]
print("Element at even-index positions from list two")
print(even_elements)

print("Printing Final third list")
l3.extend(odd_elements)
l3.extend(even_elements)
print(l3)



# Exercise 2: Remove and add item in a list
# Write a program to remove the item present at index 4 and add it to the 2nd position and at the end of the list.
# Given:

list1 = [54, 44, 27, 79, 91, 41]
selected_item = list1.pop(4)
print("List After removing element at index 4 \n" , list1)
list1.insert(2, selected_item)
print("List After adding element at index 2 \n" , list1)
list1.append(selected_item)
print("List After adding element at last \n" , list1)


# Exercise 3: Slice list into 3 equal chunks and reverse each chunk
# Given:

sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

total = len(sample_list)
partitions = int(total / 3)

start = 0
end = partitions

for i in range(3):
    indexes = slice(start, end)

    temp_list = sample_list[indexes]
    print("List", (i+1), temp_list)

    print("After reversing the list: \n", list(reversed(temp_list)))

    start = end
    end += partitions


# Exercise 4: Count the occurrence of each element from a list
# Write a program to iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element.
# Given:

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
max_num = max(sample_list)
count_dic = {}

for i in range(max_num):
    validation = sample_list.count(i)
    if validation != 0:
        count_dic[i] = sample_list.count(i)
    else:
        pass
print("Printing count of each item \n" ,count_dic)



# Exercise 5: Create a Python set such that it shows the element from both lists in a pair
# Given:

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

zipped_list = set(zip(first_list, second_list))
print(zipped_list)


# Exercise 6: Find the intersection (common) of two sets and remove those elements from the first set
# Given:

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}

inner_set = first_set & second_set; inner_set

for i in inner_set:
    first_set.remove(i)
print("The first set excluding the second_set values: \n", first_set)


# Exercise 7: Checks if one set is a subset or superset of another set. If found, delete all elements from that set
# Given:

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

print("First set is subset of second set -", first_set.issubset(second_set))
print("Second set is subset of First set - ", second_set.issubset(first_set))

print("First set is superset of second set -", first_set.issuperset(second_set))
print("Second set is superset of First set - ", second_set.issuperset(first_set))

if first_set.issubset(second_set):
    first_set.clear()

if second_set.issubset(first_set):
    second_set.clear()

print("First Set ", first_set)
print("Second Set ", second_set)

# Exercise 8: Iterate a given list and check if a given element exists as a key’s value in a dictionary. If not, delete it from the list
# Given:

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

for i in roll_number:
    if i in sample_dict:
        pass
    else:
        roll_number.remove(i)

print("After removing unwanted elements from list \n", roll_number)

# Exercise 9: Get all values from the dictionary and add them to a list but don’t add duplicates
# Given:

speed = {'jan': 47, 'feb': 52, 'march': 47, 'April': 44, 'May': 52, 'June': 53, 'july': 54, 'Aug': 44, 'Sept': 54}

temp_set = sorted(set(speed.values()))

print(temp_set)


# Exercise 10: Remove duplicates from a list and create a tuple and find the minimum and maximum number
# Given:

sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

sample_list_1 = sample_list[:]

sample_list_1 = tuple(sorted(set(sample_list_1)))
print("The tuple with unique values \n", sample_list_1)
print("Max value: ", max(sample_list_1))
print("Min value: ", min(sample_list_1))