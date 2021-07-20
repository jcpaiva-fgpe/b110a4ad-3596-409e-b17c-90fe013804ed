collection = set(('Thorgal. Part I', 'Thorgal. Part II', 'Kayko and Kokosh. Part I',  'Kayko and Kokosh. Part II' ))
thorgal = set(('Thorgal. Part I', 'Thorgal. Part II', 'Thorgal. Part III' ))
kayko = set(('Kayko and Kokosh. Part I',  'Kayko and Kokosh. Part II' ))
print('You are a lucky owner of following Kayko and Kokosh series:')
for t in kayko.union(collection):
    print(t)
if collection >= thorgal:
    print('You have the complete Thorgal series.')
else:
    print ('You are missing the following Thorgal series:')
    for t in thorgal.symmetric_difference(collection):
        print(t)