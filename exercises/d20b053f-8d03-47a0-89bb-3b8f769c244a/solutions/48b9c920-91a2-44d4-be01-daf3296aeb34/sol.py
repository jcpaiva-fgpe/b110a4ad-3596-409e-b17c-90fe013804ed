wrong = 0

while wrong < 3:
    print('Code?')
    code = input()

    if code == 'Yummy!':
        print('True!')
        break
    else:
        wrong +=1
        if wrong == 3:
            print('False!') 
            break

        print(False)