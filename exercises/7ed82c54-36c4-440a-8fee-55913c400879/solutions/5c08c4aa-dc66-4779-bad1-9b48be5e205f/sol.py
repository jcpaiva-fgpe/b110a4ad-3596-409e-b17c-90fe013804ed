print('Enter text with underscores:')
txt = input()

while txt.count('_') % 2 == 0:
    if txt.count('_') == 0: break
    upword = str(txt[txt.find('_')+1:txt.find('_', txt.find('_')+1)]).upper()
    txt = txt[:txt.find('_')] + upword + txt[txt.find('_', txt.find('_')+1)+1:]

print('Text after modification:')
print(txt)