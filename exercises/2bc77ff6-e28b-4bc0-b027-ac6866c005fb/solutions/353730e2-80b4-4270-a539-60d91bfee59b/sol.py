age = int(input('How old are you?\n'))

while age < 18:
    print(f'Still {18-age} years until the age of majority.')
    age = input('How old are you now?\n')
print('Finally adult!')