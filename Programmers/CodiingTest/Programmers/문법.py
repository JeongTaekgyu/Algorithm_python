str = "asdf"

print(len(str)/2)
print(str[2])
print(str[int(len(str)/2)])
print(type(len(str)))

alist = []
alist.append(1)
alist.append([3,4])
print(alist)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:
	if fruit == '사과':
		count += 1

print(count)

# 사과의 개수를 세어 보여줍니다.