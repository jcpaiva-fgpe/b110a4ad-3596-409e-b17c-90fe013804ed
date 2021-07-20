collection = set(('Thorgal. Part I', 'Thorgal. Part II', 'Kayko and Kokosh. Part I',  'Kayko and Kokosh. Part II' ))
thorgal = set(('Thorgal. Part I', 'Thorgal. Part II', 'Thorgal. Part III' ))
kayko = set(('Kayko and Kokosh. Part I',  'Kayko and Kokosh. Part II' ))
print('You are a lucky owner of following Kayko and Kokosh series:')
for t in kayko.intersection(collection):
    print(t)
if thorgal <= collection.intersection(thorgal):
    print('You have the complete Thorgal series.')
else:
    print ('You are missing the following Thorgal series:')
    for t in thorgal.symmetric_difference(thorgal.intersection(collection)):
        print(t)
