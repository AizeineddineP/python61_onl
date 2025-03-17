import re

lines = ["I love my cat", "This is a category", "dog is not a ca!"]
for line in lines:
    if re.search(r"cat", line):
        print(line)

print("!!!SPACE!!!")

lines = ["abz123z", "zzzz", "azzzb", "z12z", "zabczz"]
for line in lines:
    if re.search(r"z.{3}z", line):
        print(line)

print("!!!SPACE!!!")

numbers = ["8123456789", "9123456789", "7123456789", "823456789"]
pattern = r"^[89]\d{9}$"

for number in numbers:
    if re.fullmatch(pattern, number):
        print(number)

print("!!!SPACE!!!")

text = "Apple is a great fruit. Orange is good for juice. Strawberry and ananas are so good!"
pattern = r"\b[aeiouAEIOU]\w*"

print(re.findall(pattern, text))

print("!!!SPACE!!!")

text = "I have -20 apples and 15 oranges, but my friend has -5 bananas. We all have 26 ananas"
pattern = r"-?\d+"

print(re.findall(pattern, text))

print("!!!SPACE!!!")

lines = ["I am human", "This is a human error", "humankind is evolving"]
for line in lines:
    print(re.sub(r"human", "computer", line))

print("!!!SPACE!!!")

text = "Today's date is 13-03-2025, and tomorrow will be 14-03-2025. And after on year it will be 13.03.2026."
pattern = r"\b\d{2}-\d{2}-\d{4}\b"

print(re.findall(pattern, text))

print("!!!SPACE!!!")

text = "Bob bought a big blue balloon"
pattern = r"\b\w*b\w*\b"

print(re.findall(pattern, text, re.IGNORECASE))

print("!!!SPACE!!!")

text = "Sooo greaaaaat! Cooooomputerrrrr! ooohhh!"
pattern = r"(.)\1+"

print(re.sub(pattern, r"\1", text))

print("!!!SPACE!!!")

