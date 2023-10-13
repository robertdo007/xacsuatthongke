file_path = "/Users/omanee/Desktop/Xacsuatthongke/data.txt"
file = open(file_path, "r")
###############################
import re

def search_and_display_next_chars(string_list, search_substring, num_chars):
    pattern = re.compile(f"{re.escape(search_substring)}(.{{0,{num_chars}}})")
    
    for string in string_list:
        matches = pattern.finditer(string)
        for match in matches:
            next_chars = match.group(1)
            print(next_chars)

# Example usage



# List of strings
strings = []
with open(file_path, "r") as file:
    # Read each line and add it to the list
    for line in file:
        strings.append(line.strip())
        
################
count = len(strings)

# Print the count
print("Number of elements in the list:", count)
##############
#####################
search_substring =  "b b b t b b t b b "
num_chars = 30

search_and_display_next_chars(strings, search_substring, num_chars)
main_list = []  # The main list to which you want to add the result list


counts = {}

# Iterate over each element in the list
for element in main_list:
    first_char = element[0]  # Get the first character of the element

    # Check if the first character exists as a key in the dictionary
    if first_char in counts:
        counts[first_char] += 1  # Increment the count if the key exists
    else:
        counts[first_char] = 1  # Set the count to 1 if the key doesn't exist

# Print the counts
for char, count in counts.items():
    print(f"Character '{char}': {count} occurrence(s)")

import re

def count_characters_after_substring(string_list, search_substring):
    pattern = re.compile(f"{re.escape(search_substring)}(.)")
    character_counts = {}

    for string in string_list:
        matches = pattern.finditer(string)
        for match in matches:
            character = match.group(1)
            if character in character_counts:
                character_counts[character] += 1
            else:
                character_counts[character] = 1

    return character_counts

result = count_characters_after_substring(strings , search_substring)
print(result)






