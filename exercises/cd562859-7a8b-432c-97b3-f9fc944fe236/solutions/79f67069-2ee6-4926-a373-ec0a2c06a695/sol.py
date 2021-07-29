txt = input('Text?\n')
uniq = set()
for i in txt:
    uniq.update(i)
    
print(txt,'consists of', len(uniq), 'characters.')