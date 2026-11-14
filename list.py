#l(start:stop-1;jump)

l = [1,2,3,4,5,6,7,8,9]
l[0] = 300

print(l)

for i in l:
    print(i)

name =["John","Jane","Doe","Smith","Doe"]

for n in name:
    print(n)
    if n == "Doe":
        print("Found Doe")
        continue


l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

for i in l:
    print("I value is",i)
    if i == 15:         # conditions စစ်မှာ
        print("Found 15")
        print(i)
        l[l.index(i)] = 38 #l[l.index(15)] = 38 ===> l[13] = 38

print("After replacing 15 with 38")
print(l)

x = range(3)
print(x)