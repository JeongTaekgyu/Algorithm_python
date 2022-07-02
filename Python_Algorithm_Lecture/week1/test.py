def findtest(string):
    alphabet = [0] * 26

    # print(range(len(string)))
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        print(arr_index)
        print(chr(arr_index + ord("a")))

    return "리턴값이다"

print(findtest("sklhrk"))