age = input('How old are you?\n')

while int(age) < 18:
    print('Still underage.')    
    
    age = input('How old are you now?\n')
    print('Finally adult!')
