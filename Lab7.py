# Program Name: lab7.py 
# Course: IT3883/Section 01
# Student Name: Ryan Shah, Antonio Samms, & Louis Anleu Lopez
# Assignment Number: Lab7
# Due Date: 12/5/ 2023


import re

# Initialize an empty list
word_list = []

# Open the speech text file
with open('speech.txt', 'r') as file:
    # Read the file
    text = file.read()
    # Find all occurrences of 'the' followed by a word
    matches = re.findall(r'\bthe\b (\w+)', text, re.IGNORECASE)
    # Add the following word to the list
    word_list.extend(matches)

# Print out the list to a file
with open('output.txt', 'w') as file:
    for word in word_list:
        file.write(word + '\n') 
