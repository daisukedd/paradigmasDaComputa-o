def count_characters(input_string):
    return len(input_string)

while True:
     input_string = input("Enter a string: ")
     if not input_string.isdigit():
         break
     print("Please enter a valid string, not a number.")
character_count = count_characters(input_string)
print("Number of characters:", character_count)