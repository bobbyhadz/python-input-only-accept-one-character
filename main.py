# Only accept a single character from user Input in Python

user_input = ''

while True:
    user_input = input('Enter a single character: ')

    if len(user_input) == 1:
        print(user_input)
        break

    else:
        print('Enter a single character to continue.')
        continue

# 👇️ if you need to convert the character to lower or uppercase
print(user_input.lower())
print(user_input.upper())