a = ["a","b","c","d"]
print(a)
b = a
for i in range(0,4) :
    a.pop(0)
    print(b)
print(b)
print(a)