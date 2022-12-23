import math
int("123")
Y=int(input("년도를 입력하세요: "))
M=int(input("월을 입력하세요: "))
D=int(input("일을 입력하세요: "))
dayOfYear = (M-1) * 31 + D
if M < 3:
    print("통일:", dayOfYear)
elif M >= 3:
    if Y % 400 == 0:
        print("통일:", dayOfYear - ((4 * M + 23) // 10)+1)
    elif Y % 4 == 0:
        if Y % 100 == 0:
            print("통일:", dayOfYear - ((4 * M + 23) // 10))
        else:
            print("통일:", dayOfYear - ((4 * M + 23) // 10)+1)
    else:
        print("통일:", dayOfYear - ((4 * M + 23) // 10))
            
