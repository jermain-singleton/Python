with open('PythonLearned.txt') as file_object:
    lines = file_object.readlines()  # stores the text in this variable
    # contents = file_object.read()
    # print(contents)

# for line in lines:  # loop through each line of text
#     print(line.rstrip())  # print the lines with the newline strip out
# The below prints loops through lines removed newlines and add space with regex after period
import re
Py_string = ''
for line in lines:
    Py_string += line.strip() 
s = Py_string
s = re.sub('([.])', r'\1 ', s)
print(s)

#print(Py_string)
print(len(Py_string))