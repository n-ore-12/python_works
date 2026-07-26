
my_str = "Hello"
my_float = 6.22
my_bool = True
my_int = 3

my_list = [2, 3, 5]
my_list2 = [5, 1, 2]
result = [a - b for a,b in zip(my_list, my_list2)]
result2 = [a / b for a,b in zip(my_list, my_list2)]

my_tuple = (4, 9, 1)

my_dict = {"a1": 5, "a2": 10, "a3": 15}


print(my_list[1])

print(my_dict["a1"])

x = 121 % 3 
print(x)

print(4 == 1)
print(4!=1)
print(4>1)
print(result2)