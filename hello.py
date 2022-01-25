import numbers


print("hello")

a = 3
b = 4
print(a**b)

a = "Hello world"

print(type(a))

a = "python"
b = " is fun!"
print(a+b)

a = "python"
b = " is fun!"
print(a * 1)

a = "Life is too short, Ydu need python"
print(a[0:4])

a = "12345678"
print(a[::2]) 

a = "I eat %d apples. " %3
b = '12123425125'
print(b[::-2])

number = 10
day = "three"
a = "I ate %d apples. so I was sick for %s days." % (number, day)
print(a)

a = "hobby"
print(a.find('x'))

a = ",".join("abcd")
print(a)

a = ",".join(["a","b","c"])
print(a)

t1 = (1,2,'a','b')
t2 = (3,4)
print(t1*3)

t1 = (1,2,'a','b')
print(t1[0] + 1)
a =(1,2)
a = a * 3
print(a)

dic = {'name': '박은서', 'age':11}
print(dic['name'])

a = {1: 'a'}
a['name'] = "익명"
print(a)

s1 = set("Hello")
print(s1)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1.intersection(s2))

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1.union(s2))
print(s2.union(s1))


