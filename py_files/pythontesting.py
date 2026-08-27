
b = 7
type(b)
print(type(b))

list2 = ('red', "white", "hello,", "never", "me")

print(list2[2:5])

list2_new = [item.replace('r','o') for item in list2]

print(list2_new)

a = "my name is"

a1 = a.replace("m", "p")
print(a1)