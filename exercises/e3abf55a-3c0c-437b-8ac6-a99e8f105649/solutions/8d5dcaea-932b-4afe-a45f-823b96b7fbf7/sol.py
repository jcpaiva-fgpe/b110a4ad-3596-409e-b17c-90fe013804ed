print('Write the 1st text:')
txt1 = input()
print('Write the 2nd text:')
txt2 = input()

common = set(txt1).intersection(set(txt2))
print('Common letters are:', common)