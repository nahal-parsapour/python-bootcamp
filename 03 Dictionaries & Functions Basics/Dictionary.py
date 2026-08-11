# learn about dictionary

user = {
    "name": "Nahal",
    "age": 32,
    "skills": ["Python", "AI", "Machine learning"],
}
print("User info:", user)

user["city"] = "Tehran"
del user ["age"]
user.pop("city")
print("User info:", user)

profile  = {
    "personal": {"name": "Nahal", "country": "Iran"},
    "education": {"degree": "ai", "level": "master"},
}
print("Nested profile:", profile)

keys = ["name", "age", "city"]
values = ["Nahal", 32, "Tehran"]
combined = dict(zip(keys, values))
print("Combined dict:", combined)

text = "python is awesome and easy to learn"
counter = {}
for word in text.split():
    counter[word] = counter.get(word, 0) + 1
print("word counter:", counter)