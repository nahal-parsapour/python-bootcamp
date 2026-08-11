# loops (for/while)

print("for loop example: ")
for i in range(1, 6):
    print("Number:", i)

print("\nwhile loop example: ")
count = 1
while count <= 5:
    print("Count:", count)
    count += 1



# string_counter

text = input("Enter a word: ")

print("Characters:")
for char in text:
    print(char)

print("\nCounting characters with while:")
index = 0
while index < len(text):
    print(f"Index {index}: {text[index]}")
    index += 1