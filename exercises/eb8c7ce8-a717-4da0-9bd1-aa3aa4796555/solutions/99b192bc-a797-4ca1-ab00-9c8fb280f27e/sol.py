print("Enter a number:")
x = int(input())

if 10 <=x <=100 and x%3==0: #range from 10 to 100 and is divisible by 3
    print('Matches both conditions.')
else:
    print('Does not match both conditions at once.')