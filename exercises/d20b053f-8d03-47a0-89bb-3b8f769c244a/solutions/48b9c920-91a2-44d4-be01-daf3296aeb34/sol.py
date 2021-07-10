wrong = 0

while wrong < 3:
    print('Enter the secret lunch code:')
    code = input()

    if code == 'Yummy!':
        print('That\'s a good one!')
    else:
        wrong +=1
        if wrong == 3:
            print('Maximum number of login attempts has been reached.') 
            break

        print('That\'s not good.')