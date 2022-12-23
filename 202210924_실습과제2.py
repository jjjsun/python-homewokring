import math
float("123.2")
Ad=float(input("쇼핑몰 A까지의 거리를 km단위로 입력하세요:"))
Ap=float(input("쇼핑몰 A의 컴퓨터 가격을 입력하세요:"))
Ac=Ap+(190*Ad+9160/40*Ad)*2
print("쇼핑몰 A에서 구매는 전체비용은", Ac, "입니다.")
Bd=float(input("쇼핑몰 B까지의 거리를 km단위로 입력하세요:"))
Bp=float(input("쇼핑몰 B의 컴퓨터 가격을 입력하세요:"))
Bc=Bp+(190*Bd+9160/40*Bd)*2
print("쇼핑몰 A에서 구매는 전체비용은", Bc, "입니다.")
Cp=float(input("온라인 컴퓨터 가격을 입력하세요:"))
Ct=float(input("택배 비용을 입력하세요:"))
Cc=Cp+Ct
print("온라인 쇼핑몰에서 구입하는 전체 비용은", Cc, "입니다.")
k = min(Ac,Bc,Cc)
if k == Ac == Bc == Cc:
    print("C 쇼핑몰에서 구입하는 것이 좋습니다")
elif k == Ac == Cc:
    print("C 쇼핑몰에서 구입하는 것이 좋습니다")
elif k == Bc == Cc:
    print("C 쇼핑몰에서 구입하는 것이 좋습니다")
elif k == Ac == Bc:
    print("A 쇼핑몰 또는 B 쇼핑몰에서 구입하는 것이 좋습니다")
elif k == Ac:
    print("A 쇼핑몰에서 구입하는 것이 좋습니다")
elif k == Bc:
    print("B 쇼핑몰에서 구입하는 것이 좋습니다")
elif k == Cc:
    print("C 쇼핑몰에서 구입하는 것이 좋습니다")
