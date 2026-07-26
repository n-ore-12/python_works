import subprocess

my_list = (1, 2, 4, 5, 6, 3, 0)

command = "touch /Users/eduan/work/testing/output.txt"

#for i in range(len(my_list)):
    #path = f"/Users/eduan/work/testing/output{i}.txt"
   # subprocess.run(["touch", path])


x = 5
for i in range(20):
    x+=1
    if x > 15:
        print("hello")
    else:
        print("bye")


y = 99

while y < 110:
    print(y)
    y+= 1

