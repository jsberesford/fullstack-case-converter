camel = input("Enter camelCase:")

snake = ""
for char in camel:
    if char.islower():
        snake += char
        continue
    if char.isupper():
        snake +=  "_" + char
        continue
    if char.islower():
        snake += char
snake = snake.lower()
print(snake)





