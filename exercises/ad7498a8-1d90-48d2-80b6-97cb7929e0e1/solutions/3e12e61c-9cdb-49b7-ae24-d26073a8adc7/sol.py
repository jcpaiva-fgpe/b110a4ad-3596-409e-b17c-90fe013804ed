l = list(range(5)) + [3]
naj = 0
for e in l:
    if l.count(e) > naj: naj += 1
    
print('Najczęściej występującą wartością jest:', e)