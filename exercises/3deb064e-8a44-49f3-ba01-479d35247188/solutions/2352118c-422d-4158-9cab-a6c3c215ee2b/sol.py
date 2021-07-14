print('Enter text with parentheses:')
txt = input()
if txt.count('(') + txt.count(')') == 2:
    print('Text after removing parentheses:')
    txt = txt[:txt.find('(')+1] + txt[txt.rfind(')'):]
print(txt)