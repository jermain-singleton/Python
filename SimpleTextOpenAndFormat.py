""" program to open a text files read the lines, save output to a variable and format a bit """
with open('PythonLearned.txt') as file_object:    #opens the file and a with close() is not needed here
    lines = file_object.readlines()  # stores the text in this variable 
    # contents = file_object.read()  #stores lines to a variable
    # print(contents)

# for line in lines:  # loop through each line of text
#     print(line.rstrip())  # print the lines with the newline strip out
# The below prints loops through lines removed newlines and add space with regex after period
import re  #imports regex module
Py_string = ''  #creates a empty variable
for line in lines:  #loop
    Py_string += line.strip()  #adds lines to the new variable and strips the newline print
s = Py_string # creates a new variable for regex condition
s = re.sub('([.])', r'\1 ', s) #regex sub . and close off the space where r'\1', s
print(s)

#print(Py_string)
print(len(Py_string))  # prints the length of original create string variable
