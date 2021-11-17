#fah_convert()
#from myconvert import fah_convert
import myconvert

print('섭씨온도를 입력하세요!')
user_input = input()
result = myconvert.fah_convert(user_input)
#conv.fah_convert()

print('화씨온도는 ', result, '입니다')
print('섭씨온도는 {} 화씨온도는 {:.2f} 입니다.'.format(user_input,result))
print(f'섭씨온도는 {user_input} 화씨온도는 {result:.2f} 입니다.')

