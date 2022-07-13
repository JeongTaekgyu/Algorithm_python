s = 'python is fun'
c = 'n'
lst = []
for pos,char in enumerate(s):
    if(char == c):
        lst.append(pos)
print(lst)