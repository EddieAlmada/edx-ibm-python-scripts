# https://pynative.com/python-dictionary-exercise-with-solutions/

#################### Exercise 1: Convert two lists into a dictionary ####################
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
dict_var = {}
temp_list = []

for i in zip(keys,values):
    temp_list.append(i)

dict_var = dict(temp_list)
print("Printing dictionary: \n", dict_var)

res_dict = dict(zip(keys, values))
print(res_dict)

#################### Exercise 2: Merge two Python dictionaries into one ####################
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}


dict3 = dict1.copy()
dict3.update(dict2)
print("Printing dictionary: \n", dict3)

 
#################### Exercise 3: Print the value of key ‘history’ from the below dict ####################

sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}


history_score = sampleDict['class']['student']['marks']["history"]
print("My history score is:", history_score)

#################### Exercise 4: Initialize dictionary with default values ####################

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

new_dict = dict.fromkeys(employees, defaults)
print("Answer: \n", new_dict)

#################### Exercise 5: Create a dictionary by extracting the keys from a given dictionary ####################

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]
final_dict = {}

for i in keys:
    final_dict.update({i:sample_dict[i]})
    
print("Answer: \n", final_dict)

#################### Exercise 6: Delete a list of keys from a dictionary ####################

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
new_dict = sample_dict.copy()

# Keys to remove
keys = ["name", "salary"]

for i in keys:
    new_dict.pop(i)

print("Answer: \n", new_dict)

#################### Exercise 7: Check if a value exists in a dictionary ####################
# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.
# Write a Python program to check if value 200 exists in the following dictionary.
# Given:

sample_dict = {'a': 100, 'b': 200, 'c': 300}

if 200 in sample_dict.values():
    print("200 IS present in the dictionary")
else:
    print("200 is MOT in the dict")


#################### Exercise 8: Rename key of a dictionary ####################

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

sample_dict["location"] = sample_dict.pop("city")

print("Answer: \n", sample_dict)

#################### Exercise 9: Get the key of a minimum value from the following dictionary ####################

sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

print("Answer: \n", min(sample_dict))

#################### Exercise 10: Change value of a key in a nested dictionary ####################

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

sample_dict["emp3"]["salary"] = 8500

print("Answer: \n", sample_dict)