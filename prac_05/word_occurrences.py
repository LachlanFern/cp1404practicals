"""
Word Occurrences
Estimate: 40 mins
Actual: 30 mins
"""

dictionary = {}
text =  input("please input a sentence: ").lower()
words = text.split()
long_word = ""
width = 0

for word in words:
    dictionary[word] = dictionary.get(word, 0)+1
    if len(word) > len(long_word):
        long_word = word
    width = len(long_word)


for word, count in dictionary.items():
    print(f"{word:{width}}: {count}")