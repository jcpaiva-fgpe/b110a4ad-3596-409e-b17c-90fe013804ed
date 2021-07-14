print("Enter some text:")
txt = input()

txt = max(txt.split(), key = len)
print("The longest string is:", txt)