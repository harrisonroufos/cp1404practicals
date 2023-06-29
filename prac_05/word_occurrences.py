"""
CP1404 Practical
Word Occurrences
Estimate: 20 minutes
Actual:
"""
word_to_count = {}
text = input("Text: ")
words = sorted(text.split())
for word in words:
    if word not in word_to_count:
        word_to_count[word] = 1
    else:
        word_to_count[word] += 1

for word, count in word_to_count.items():
    print(f"{word} : {count}")
