age = int(input('How old are you?\n'))

while age < 18:
    print('Underage.')    
    
    age = input('How old are you now?\n')
    print('Finally adult!')
