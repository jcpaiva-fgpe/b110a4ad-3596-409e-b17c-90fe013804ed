todos = ['washing', 'vacuuming', 'ironing', 'cooking']

while todos:
    job = input ('Now what?\n')
    todos.remove(job)

print('All done! Have a nice rest!') 