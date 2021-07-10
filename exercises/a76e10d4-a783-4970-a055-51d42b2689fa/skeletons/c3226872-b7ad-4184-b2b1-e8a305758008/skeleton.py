kolekcja = set(('Thorgal. Tom I', 'Thorgal. Tom II', 'Kajko i Kokosz. Tom I',  'Kajko i Kokosz. Tom II' ))
thorgal = set(('Thorgal. Tom I', 'Thorgal. Tom II', 'Thorgal. Tom III' ))
kajko = set(('Kajko i Kokosz. Tom I',  'Kajko i Kokosz. Tom II' ))
print u'Masz następujące tomy Kajko i Kokosza:'
for t in kajko.union(kolekcja):
    print t
if kolekcja >= thorgal:
    print 'Masz wszystkie tomy Thorgala.'
else:
    print u'Brakuje Ci następujących tomów Thorgala:'
    for t in thorgal.symmetric_difference(kolekcja):
        print t