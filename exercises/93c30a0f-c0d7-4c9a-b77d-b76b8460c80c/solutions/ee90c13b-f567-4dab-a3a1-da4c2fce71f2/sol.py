zdanie1 = input().split()
zdanie2 = input().split()
print('Takie same wyrazy to:', *list(set(in1) & set(in2)))
