# String Methods

text = input("Type text: ")

print("Length:", len(text))
print("Words:", len(text.split()))
print("Characters:", len(text.encode("ascii", "ignore").decode("ascii")))
print("Uppercase:", text.upper())
print("Contains digit:", any(ch.isdigit() for ch in text))
print("First char:", text[0])
print("Last char:", text[-1])