# Even number with Generators
def even_numbers():
    for num in range(0, 101, 2):
        yield num

for num in even_numbers():
    print(num)


# charactor of string with Generators
def char_generator(text):
    for ch in text:
        yield ch

for c in char_generator("Nahal"):
    print(c)


# chunk a list with Generators
def chunk_generator(list):
    for i in range(0, len(list), 10):
        yield list[i:i+10]

big_list = list(range(1, 51))

for chunk in chunk_generator(big_list):
    print(chunk)
