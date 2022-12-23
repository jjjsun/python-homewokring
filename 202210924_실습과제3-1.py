import math
int("123")
k=int(input("년도를 입력하세요: "))
if k % 400 == 0:
    print(str(k), "는 윤년입니다")
elif k % 4 == 0:
    if k % 100 == 0:
        print(str(k), "은 윤년이 아닙니다")
    else:
        print(str(k), "은 윤년입니다")
else:
    print(str(k), "은 윤년이 아닙니다")
