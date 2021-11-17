#from bmi import print_bmi
import mycode.lab.bmi as bmi

def main():
    print("이름을 입력하세요")
    name = input()

    print("키(cm)를 입력하세요")
    height_cm = int(input())

    print("몸무게를 입력하세요")
    weight = int(input())

    bmi.print_bmi(name, height_cm, weight)
    #print_bmi(name,height_cm, weight)

print(__name__)
if __name__ == "__main__":
    main()