import math

n1=0

def readNumber():
    n=int(input("2이상의 정수 한 개를 입력하시오"))
    while n < 2 :
        n = int(input("2이상의 정수 한 개를 입력하시오"))
        if n >= 2:
            getDivisors()

def isprime():
    if n1 == 2:
        return True
    else:
        return False

def getDivisors():
    global n1
    for i in range(1,n+1):
        while n == i:
            if n % i == 0:
                n1 += 1
                if n1 == 2:
                    print("정수: ",n ,"약수 개수: ",n1, "소수: ",isprime())

readNumber()

