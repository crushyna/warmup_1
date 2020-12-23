def fun(input_string: str) -> [str, str]:
    return_string_1 = ""
    return_string_2 = ""
    i = True
    for each_char in input_string:
        if i:
            return_string_1 += each_char.upper()
            return_string_2 += each_char.lower()
        else:
            return_string_1 += each_char.lower()
            return_string_2 += each_char.upper()
        if each_char != ' ':
            i = not i

    return [return_string_2, return_string_1]


input_string = input("Enter your string to have some fun:")
if not input_string.isalpha():
    print("Not a string. Only strings without spaces are acceptable.")

else:
    result = fun(input_string)
    print(result)
