# File Creation:
# Create a Python script (file_handling_assignment.py)
# that does the following:
# Creates a new text file named "my_file.txt" in write
# mode ('w').
# Write at least three lines of text to the file,
# including a mix of strings and numbers.
# File Reading and Display:
# Enhance your script to read the contents of "my_file.txt"
# and display them on the console.
# File Appending:
# Modify the script to open "my_file.txt" in append mode
# ('a').
# Append three additional lines of text to the existing
# content.
# Error Handling:
# Implement error handling using try, except, and finally
# blocks to manage potential file-related exceptions
# (e.g., FileNotFoundError, PermissionError).

# create variable to store text file
file_path = "my_file.txt"

# Open file in write mode
with open(file_path, "w") as file:
    #write at least three lines of text
    file.write("Hello there.\n")
    file.write("I'm Kiarie.\n")
    file.write("Programming is challenging but rewarding.\n")
    file.write("500.\n")

#Read the contents of my_file.txt
file_path = open("my_file.txt", "r")

#Display contents of my_file.txt
print(file_path.read())

#modify script to open file in append mode
file_path = open("my_file.txt", "a")

#append 3 additional lines
file_path.write("Today is Sunday.\n")
file_path.write("9th Nov.\n")
file_path.write("Year is 2024.\n")

#output after appending
file_path = open("my_file.txt", "r")
print(file_path.read())

#Error handling - FileNotFoundError
try:
    file = open("my_file.txt", "r")
    content = file.read()
    print(content)
    file_path.close()
except FileNotFoundError:
    print("The file does not exist!")

#Error handling - PermisionError
try:
    file = open("my_file.txt", "w")
    file.write("Confidential info")
    file_path.close()
except PermissionError:
    print("You don't have permission to write in this file!")

#Error handling - IOError
try:
    file = open("my_file.txt", "r")
    content = file.read()
    print(content)
    file_path.close()
except IOError:
    print("An error occured while reading the file!")
