print('String 1?')
txt1 = input()
print('String 2?')
txt2 = input()

common = set(txt1).intersection(set(txt2))
print('Common characters:', common)