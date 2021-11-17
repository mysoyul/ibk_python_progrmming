
def print_bmi(name,height_cm, weight):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)

    print(f'{name}님의 BMI 수치는 {bmi:.1f} 입니다')