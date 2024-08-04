print("####################### Exercise 1 ##########################")

def multiplication_or_sum(number1,number2):

    if number1*number2 <= 1000:
        return print("The result is:",number1 * number2)
    else:
        return print("The result is:", number1 + number2)

multiplication_or_sum(20,30)
multiplication_or_sum(40,30)

print("####################### Exercise 2 ##########################")

previous_num  = 0

for i in range(10):
    x_sum = previous_num + i
    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", x_sum)
    # modify previous number
    # set it to the current number
    previous_num = i

print("####################### Exercise 3 ##########################")

# user_text = input("Type a string value: ")

user_text = 'pynative'

size = len(user_text)

# iterate a each character of a string
# start: 0 to start with first character
# stop: size-1 because index starts with 0
# step: 2 to get the characters present at even index like 0, 2, 4
print("\nPrinting only even index chars")
for i in range(0, size - 1, 2):
    print("index[", i, "]", user_text[i])

print("####################### Exercise 4 ##########################")

def remove_chars(text_var,num_var):
    output = text_var[num_var:]
    return output

print("Removing characters from a string")
print(remove_chars("pynative", 4))


print("####################### Exercise 5 ##########################")

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

def first_last_check(list_input):
    if list_input[0] == list_input[-1]:
        print("result is true")
    else:
        print("result is false")

first_last_check(numbers_x)
first_last_check(numbers_y)


print("####################### Exercise 6 ##########################")

var =  [10, 20, 33, 46, 55]

for i in var:
    if (i % 5) == 0:
        print(i)
    else:
        pass

print("####################### Exercise 7 ##########################")

str_x = "Emma is good developer. Emma is a writer"

list_var = str_x.split(" ")

print("No of times Emma appears in text" ,list_var.count("Emma"))


print("####################### Exercise 8 ##########################")


for i in range(1,6):
    print(str(i)*i)

print("####################### Exercise 9 ##########################")

def tacocat(inp_var):
    if str(inp_var) == str(inp_var)[::-1]:
        print("We've got a palindrome")
    else:
        print("No palindrome :(")

tacocat(1221)
tacocat(1231)

print("####################### Exercise 10 ##########################")

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
new_list = []

for i in list1:
    if i % 2 == 0:
        pass
    else:
        new_list.append(i)

for i in list2:
    if i % 2 != 0:
        pass
    else:
        new_list.append(i)

print(new_list)


print("####################### Exercise 11 ##########################")

def rev_num(num_var):
    rev = str(num_var)[::-1]
    return print(rev)


rev_num(7536)