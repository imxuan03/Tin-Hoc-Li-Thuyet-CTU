import re
# string = 'Computer science 2020 and Software Engineering 2023'
# pattern = '\d+'
# result = re.findall(pattern, string)
# print(result)

# wood ='how much wood would a woodchuck chuck if a woodchuck chuck wood?'
# result = re.findall(r'wo\w+', wood)
# print(result)

# foo = 'This and that and those'
# result = re.findall(r'th\w+', foo)
# print(result)

# foo = 'This and that and those'
# result = re.findall(r'th\w+', foo, re.IGNORECASE)
# print(result)

# string = "Computer Science, Software Engineering"
# new_String = re.sub('\s+','',string)
# print(new_String)


# wood ='how much wood would a woodchuck chuck if a woodchuck chuck wood?'
# result = re.sub(r'[aeiou]+','-',wood)
# print(result)

# string = 'Computer science 2020 and Software Engineering 2023'
# pattern = '\d+'
# result = re.search(pattern, string)
# print(result)

string = 'Computer science 2020 and Software Engineering 2023'
pattern = '\s'
result = re.split(pattern, string, 2)
print(result)