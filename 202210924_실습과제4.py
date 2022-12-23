import math
k=input("주민등록번호를 입력하세요")
Y = str(k[:2])
M = int(k[2:4])
D = int(k[4:6])
S = int(k[6])
"k".isdigit()
Y = int(Y)
def BFFalse() :
    print("주민번호 뒷번호 첫번째 자리가 잘못 입력되었습니다")
def BFalse() :
    print("생년월일 일자가 잘못 입력되었습니다")    
def MFalse() :
    print("월이 1~12의 범위 내에 포함되지않았습니다")
def TTrue() :
    print("주민등록번호가 적합해 보입니다")
def 반환():
    return 0
def isSafterValid(k):
    if S == 3 or S == 4:
        TTrue()
    else:
        BFFalse()
        반환()
def isSbeforeValid(k):
    if S == 1 or S == 2:
        TTrue()
    else:
        BFFalse()
        반환()
def isDFebafterValid(k):
    if 1<=D and D<=29:
        isSafterValid(k)
    else:
        BFalse()
def isDFebbeforeValid(k):
    if 1<=D and D<=29:
        isSbeforeValid(k)
    else:
        BFalse()
def isDFebNafterValid(k):
    if 1<=D and D<=28:
        isSafterValid(k)
    else:
        BFalse()
def isDFebNbeforeValid(k):
    if 1<=D and D<=28:
        isSbeforeValid(k)
    else:
        BFalse()
def isBRafterValid(k):
    if 1<=D and D<=31:
        isSafterValid(k)
    else:
        BFalse()
def isBRbeforeValid(k):
    if 1<=D and D<=31:
        isSbeforeValid(k)
    else:
        BFalse()
def isthirtyafterValid(k):
    if 1<=D and D<=30:
        isSafterValid(k)
    else:
        BFalse()
def isthirtybeforeValid(k):
    if 1<=D and D<=30:
        isSbeforeValid(k)
    else:
        BFalse()
def isYOONbeforeValid(k):
    if M==2:
        isDFebbeforeValid(k)
    elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
        isBRbeforeValid(k)
    elif M==4 or M==6 or M==9 or M==11:
        isthirtybeforeValid(k)
    else:
        MFalse()

if len(k) != 13:
    print("주민등록번호가 잘못되었습니다")
else:
    if Y <= 22:
        if (Y+2000) % 4 == 0 and((Y+2000) % 100 != 0 or (Y+2000) % 400 == 0):
            if M==2:
                isDFebafterValid(k)
            elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
                isBRafterValid(k)
            elif M==4 or M==6 or M==9 or M==11:
                isthirtyafterValid(k)
            else:
                MFalse()
        else:
            if M==2:
                isDFebNafterValid(k)
            elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
                isBRafterValid(k)
            elif M==4 or M==6 or M==9 or M==11:
                isthirtyafterValid(k)
            else:
                MFalse()
    else:
        if (Y+1900) % 4 == 0 and((Y+1900) % 100 != 0 or (Y+1900) % 400 == 0):
            if M==2:
                isDFebbeforeValid(k)
            elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
                isBRbeforeValid(k)
            elif M==4 or M==6 or M==9 or M==11:
                isthirtybeforeValid(k)
            else:
                MFalse()
        else:
            if M==2:
                isDFebNbeforeValid(k)
            elif M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
                isBRbeforeValid(k)
            elif M==4 or M==6 or M==9 or M==11:
                isthirtybeforeValid(k)
            else:
                MFalse()
