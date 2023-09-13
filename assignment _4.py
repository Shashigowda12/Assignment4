size =int(input("Enter the size of the list:"))
list = []
for i in range(size):
    values = input("Enter the vlaues:")
    tuple_values=tuples(map(int, values.split(',')))
    lst.append(tuple_values)

sorted_list=[]

While_lst:
    min_tuple = lst[0]
    for t in lst:
    if t[-1]<min_tuple[-1]:
        min_tuple = t
    sorted_list.append(min_tuple)
    lst.remove(min_tuple)
print("sorted list:",sorted_list)