my_list=[]
n=int(input("enter the number of elements in the list:"))
for i in range(n):
    x=int(input("enter the number:"))
    my_list.append(x)

print(my_list)
print("({}, {})".format(my_list[0],my_list[-1]))