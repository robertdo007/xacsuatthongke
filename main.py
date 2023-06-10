file_path = "/Users/omanee/Desktop/Xacsuatthongke/data.txt"
file = open(file_path, "r")
###############################
def search_and_get_substring(strings, search_sequence):
    result = []

    for string in strings:
        index = string.find(search_sequence)
        if index != -1 and index + len(search_sequence) + 15 <= len(string):
            result.append(string[index + len(search_sequence):index + len(search_sequence) + 15])

    return result


# List of strings
strings = []
with open(file_path, "r") as file:
    # Read each line and add it to the list
    for line in file:
        strings.append(line.strip())
################

search_sequence = "b p t p p b"
#####################
result = search_and_get_substring(strings, search_sequence)

if len(result) > 0:
    print("Substrings found in the strings:")
    for substring in result:
        print(substring)
else:
    print("Search sequence not found or not enough characters following it.")







