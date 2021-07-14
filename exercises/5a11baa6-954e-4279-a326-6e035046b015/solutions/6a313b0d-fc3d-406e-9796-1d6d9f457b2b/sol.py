print('Enter text with asterisks:')
txt = input()

txt = txt.replace('*', '[Footnote]')
print('Text after asterisk replacement', txt)