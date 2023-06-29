"""
CP1404 Practical
Word Occurrences
Estimate: 20 minutes
Actual:   28 minutes
"""
word_to_count = {}
text = input("Text: ")
words = sorted(text.split())
for word in words:
    if word not in word_to_count:
        word_to_count[word] = 1
    else:
        word_to_count[word] += 1

max_length = 0
for word in words:
    if len(word) > max_length:
        max_length = len(word)

print(max_length)

for word, count in word_to_count.items():
    print(f"{word:{max_length}} : {count}")
