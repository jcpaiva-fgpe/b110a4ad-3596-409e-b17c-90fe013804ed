wrong = 0
print('Enter the secret lunch code:')
while wrong < 3:
    code = input()

    if code == 'Yummy!':
        print('That\'s a good one!')
    else:
        wrong +=1
        if wrong == 3:
            print('has been reached.') 
            break
        print('That\'s not good.')