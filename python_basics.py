test = 11
type(test)
type(1.2)
type("Hello")
int(23.45)
float(6)

# 0 equals False, other number TRUE
bool(1)

# Expressions

43 - 50
# returns only int
25 // 4
# returns float
25 / 4

25 % 4

test_1 = 1
test_1

import sys
print(sys.version)


# String Operations

Name = "pierre Bouvier"
Name[0]

Name[0:6]
Name[::2]
len(Name)
Name + " rocks"

3 * Name

print(Name + "\n rocks")
print(Name + "\t rocks")
print(Name + "\\ rocks")
print(Name + r"\n rocks")

Name.upper()
Name.lower()
Name.replace('Pierre','David')
Name.find('ier')

Name.split(" ")
# Removes leading/trailing whitespace
Name.strip()
# Proper funtion 
Name.title()