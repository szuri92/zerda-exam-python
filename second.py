# Create a function that takes a filename and a string as parameter,
# And writes the string got as second parameter into the file 10 times.
# If the writing succeeds, the function should return True.
# If any problem raises with the file output, the function should not break, but return False.
# Example: when called with the following two parameters: "tree.txt", "apple",
# the function should write "appleappleapple" to the file "tree.txt", and return True.

def write_in_text(file_name, text):
    try:
        my_file = open(file_name, 'a')
        for i in range(0, 10):
            my_file.write(text)
        my_file.close()
        return True
    except:
        return False

write_in_text('tree.tjkkjjkxt', 'apple')
print(write_in_text('tree.txt', 'apple'))
