# text analyze for practice string methods

from collections import Counter

print("Enter your text (type 'Y/y' on a new line to finish):")

lines = []
while True:
    line = input()
    if line == "y" or line == "Y":
        break
    lines.append(line)

text = "\n".join(lines)
words = text.split()

print("\nNumber of words:", len(words))

word_counts = Counter(words)
duplicates = {w for w, count in word_counts.items() if count > 1} or None
# freq = {w: words.count(w) for w in set(words)}
freq = dict(word_counts)

numbers = [int(w) for w in words if w.isdecimal()]
total_numbers = sum(numbers)

emails = [w for w in words if "@" in w and "." in w and w.index("@") < w.rindex(".")]


print("Duplicate words:", duplicates)
print("Word frequencies:", freq)
print("Numbers:", numbers)
print("total numbers:", total_numbers)
print("Emails:", emails)