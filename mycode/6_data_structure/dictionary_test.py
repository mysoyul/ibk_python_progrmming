"""
dictionary는 key:value 쌍으로 이루어진 데이터를 저장하는 자료구조
"""
my_dict = dict() # {}
my_dict = {'name': '홍길동', 'age': 20}
print(type(my_dict))

#dict를 key로 값을 조회
print(my_dict['name'])
#dict에 새로운 key와 value를 추가
my_dict['addr'] = '충주'

print(my_dict)

#print(my_dict['name1'])
result = my_dict.get('name1')
if result:
    print(result)
else:
    print('key does not exist')

if "name" in my_dict:
    print('name key가 있습니다.')

for key, value in my_dict.items():
    print(key,value)

#int(), float(), str(),
#list(), tuple(), set(), dict()
# list [ ] - 값 추가 허용
# tuple ( ) - 값 추가 허용 않함
# set { } - 중복허용 않함, 순서유지 않됨
# dict { } - key값으로 value 조회