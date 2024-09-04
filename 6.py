import string
letters = string.ascii_letters
user_input = input('Enter letters in format "a-c":').strip()

if len(user_input) == 3 and user_input[0].isalpha() and user_input[1] == '-' and user_input[2]:
    first_letter = user_input[0]
    last_letter = user_input[2]

    start_index = letters.index(first_letter)
    end_index = letters.index((last_letter))
    if start_index > end_index:
        result = (f"{letters[start_index:end_index + 1:-1]}")
        print(result)
        start_index,end_index = end_index,start_index
    else:
        result = letters[start_index:end_index+1]
        print(result)

# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA


