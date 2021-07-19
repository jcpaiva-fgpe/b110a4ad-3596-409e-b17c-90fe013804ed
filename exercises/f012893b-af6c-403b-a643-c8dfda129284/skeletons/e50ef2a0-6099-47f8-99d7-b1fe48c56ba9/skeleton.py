def register(entry):
    global log
    log += [entry]

log = []    
register("Nice nice weather. I'm fine.")
register("It's bad weather. I feel bad.")
register ("The weather is so-so. I feel average.")
print('\n'.join(log))