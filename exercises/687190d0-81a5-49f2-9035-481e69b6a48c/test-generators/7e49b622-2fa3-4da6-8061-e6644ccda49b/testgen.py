#printf $solutions/sol.py"\n10\n" | python $file

from random import choice as ch

li = ['', 'A', 'B', 'C', 'E', 'D', 'X', 'Z']

f = open(input())
source = f.read()
exec(source)


nr_of_tests = int(input())

for i in range(0, nr_of_tests):
    word_li = [ch(li)+ch(li) for i in range(len(li)+1)]
    word_li = ' '.join(word_li)
    
    f = open("tests/in" + str(i+1) + ".txt", "w+")
    f.write("%s\n" % (word_li))
    f.close()

    out = niepowtarzalne(word_li)

    f = open("tests/out" + str(i+1) + ".txt", "w+")
    f.write('\n'.join(out))
    f.close()
