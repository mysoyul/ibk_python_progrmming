#packing
my_list1 = [20,30,40]
#unpacking
n1,n2,n3 = my_list1
print(n1,n2,n3)

my_list2 = list()

my_list1.append(10)
print(my_list1)
my_list1.extend([50,60])
print(my_list1)
my_list1.insert(0,10)
print(type(my_list1))
print(my_list1)
my_list1[2] = 100
print(my_list1[0:3])

#set - 중복 허용 않함, 순서가 유지되지 않음
my_set = set(my_list1)
print(type(my_set))
print(my_set)

#typel - read only list
my_tuple = (10,20,30)
my_tuple2 = tuple()
print(type(my_tuple))
print(my_tuple)
#TypeError: 'tuple' object does not support item assignment
#my_tuple[0] = 50

num1 = (3)
num2 = (3,)
print(type(num1), type(num2))

#tuple usage
def swap(a,b):
    return (b,a)

a,b = swap(10,20)
print(a)
print(b)


