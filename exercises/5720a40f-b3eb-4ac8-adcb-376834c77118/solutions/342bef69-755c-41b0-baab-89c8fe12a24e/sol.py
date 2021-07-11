todos = ['washing', 'vacuuming', 'ironing', 'cooking']

while todos:
    job = input ('Now what?\n')
    if job not in todos: continue
    todos.remove(job)
     
print('All done! Have a nice rest!') 