# Test dictionary
word_freq = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding' :2}
print("The test dictionary is:", word_freq)
word = input("Enter the word you want to check the frequency of: ")
if word in word_freq:
    print(f"The frequency of '{word}' is: {word_freq[word]}")
else:
    print(f"'{word}' is not present in the dictionary.")
