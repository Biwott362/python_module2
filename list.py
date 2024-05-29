my_list = []

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list[1] = 15

anotherList = [50,60,70]
my_list.extend(anotherList)

my_list.pop(-1)

my_list.sort()

index_of_30 = my_list.index(30)

print( "Sorted my_list:", my_list)
print("Index of the value of 30 is:", index_of_30)
