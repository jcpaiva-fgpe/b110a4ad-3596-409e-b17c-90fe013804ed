age = input('How old are you?\n')

while int(age) < 18:
    print('Underage.')    
    
    age = input('How old are you now?\n')
    print('Finally adult!')
