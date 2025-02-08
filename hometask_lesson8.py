odd_numbers = [x for x in range(10, 100) if x % 2 != 0]
print(odd_numbers)


squares = [x**2 for x in range(1, 11)]
print(squares)


numbers = [x for x in range(100, 1000) if x % 5 == 0 and x % 3 == 0]
print(numbers)


a, b, p = map(int, input().split())
result = [x**p for x in range(a, b + 1)]
print(*result)


numbers = input().split()
filtered_numbers = [num for num in numbers if '0' in num]
print(*filtered_numbers)


words = input().split()
filtered_words = [word for word in words if word.count('a') > 2]
print(*filtered_words)


words = input().split()
upper_words = [word.upper() for word in words]
print(*upper_words)


words = input().split()
cleaned_words = []

for word in words:
    new_word = ""
    for char in word:
        if not char.isdigit():
            new_word += char
    cleaned_words.append(new_word)

print(*cleaned_words)
#