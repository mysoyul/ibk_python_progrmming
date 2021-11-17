"""
섭씨온도를 입력 받아서 화씨로 변환하기
"""

#섭씨를 화씨로 변환하는 함수
# 함수이름 - fah_convert
# 입력으로 들어오는 값을 저장하는 변수 (agument, parameter) : celsius
# return : 함수내부에서 계산한 값을 반환

def fah_convert(celsius):
    return ((9/5) * float(celsius)) + 32


print("변환하고 싶은 섭씨 온도를 입력하세요~")

#input() 함수는 사용자가 입력값을 받는 역할을 한다.
user_input = input()
print(type(user_input), user_input)
# fah_convert() 함수 호출하기
fah = fah_convert(user_input)
print(fah)

#
# print('섭씨온도 :', float(user_input))
# print(f'섭씨온도 : {user_input}')
# print('화씨온도 : {0:.2f}'.format(fah))
# print(f'화씨온도 :{round(fah,2)}')
