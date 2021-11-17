#List포함된 문자열 중에 j 가 포함된 문자열을 따로 저장한 리스트를 만들어보세요
lang_list = ['java', 'python', 'javascript', 'c#']
result_list = list()

for lang in lang_list:
    if 'j' in lang:
        print('++++' + lang)
        result_list.append(lang)
    print("----" + lang)

print(result_list)
result_list[0] = "java2"
print(result_list)

#tuple
my_tuple = (10,20,30)
#my_tuple[0] = 40

#key=value
person1 = {
    "name":"홍길동",
    "age":20
}
person2 = {
    "name":"둘리",
    "age":10
}
persons = [person1, person2]
#print(persons)

gildong = persons[0]
gil_name = gildong['name']
gil_age = gildong['age']

dooly = persons[1]
dooly_name = dooly['name']
dooly_age = dooly['age']

for person in persons:
    name = person["name"]
    age = person['age']
    print(name, age)



