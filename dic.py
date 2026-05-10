#s
words = {
    'codingal': 3,
    'is': 2,
    'amazing': 3
}

check_word = input("Enter a word to check its frequency: ")


if check_word in words:
    print(check_word, "appears", words[check_word], "times")
else:
    print("Word not found in the dictionary")