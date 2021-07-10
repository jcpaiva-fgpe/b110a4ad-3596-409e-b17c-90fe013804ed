symbols = set(('!','@','#','$','%','^','&'))
symbols.discard('$')
if '$' in symbols:
    print (u'The $ is still there!')
else:
    print (u'Uff! The $ is gone.')