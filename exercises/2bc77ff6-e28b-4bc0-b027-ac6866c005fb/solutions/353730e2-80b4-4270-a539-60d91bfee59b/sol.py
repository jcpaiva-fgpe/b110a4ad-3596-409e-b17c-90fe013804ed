age = int(input('How old are you?\n'))

while age < 18:
    print(f'You are still {18-age} under.')    
    
    age = input('How old are you now?\n')
    print('Finally adult!')
