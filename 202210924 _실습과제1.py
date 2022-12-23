import math
Humid = float(input("습도를 입력하세요"))
Temp = float(input("섭씨온도를 입력하세요"))
Dewpoint = (243.12 * (math.log(Humid/100) +(17.62*Temp)/(243.12 + Temp)))/(17.62 - (math.log(Humid/100) +(17.62*Temp)/(243.12 + Temp)))
Dewpoint = float(Dewpoint)
print(Dewpoint)
