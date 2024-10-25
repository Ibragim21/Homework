import math
# Begin31
# Tf=float(input("Please enter temperature in F "))
# Tc=(Tf-32)*(5/9)
# print(Tc)

# Begin32
# Tc=float(input("Please enter temperature in celcius "))
# Tf=(Tc/(5/9))+32
# print(Tf)

# Begin33
# X = float(input("X kg konfet necha : "))
# A = float(input("A so'm qiymatini kiriting: "))
# Y = float(input("Y kg konfet necha kg: "))

# cost_per_kg = A / X

# cost_y_kg = cost_per_kg * Y

# print(f"1 kg konfetning narxi: {cost_per_kg} so'm")
# print(f"{Y} kg konfetning narxi: {cost_y_kg} so'm")

#Begin34
# X = float(input("X kg shokolad necha: "))
# A = float(input("A so'm qiymatini kiriting: "))
# Y = float(input("Y kg konfet necha: "))
# B = float(input("B so'm qiymatini kiriting: "))
# cost_per_kg_shokolad = A / X
# cost_per_kg_konfet = B / Y
# print('1 kg shokkolad=',cost_per_kg_shokolad,'1 kg konfet=',cost_per_kg_konfet)

#Begin35
# V = float(input("Qayiqning tezligini kiriting (km/soat): "))
# U = float(input("Daryo oqimining tezligini kiriting (km/soat): "))
# T1 = float(input("Oqim bo'yicha harakat vaqti T1 ni kiriting (soat): "))
# T2 = float(input("Oqimga qarshi harakat vaqti T2 ni kiriting (soat): "))

# down_speed = V + U
# up_speed = V - U
# S = (down_speed * T1) + (up_speed * T2)
# print("Qayiqning yurgan umumiy masofasi:",S,"km")


#Begin36
# V1 = float(input("Birinchchi avtomobil tezligini kiriting (km/soat): "))
# V2 = float(input("Ikkinchisiniki tezligini kiriting (km/soat): "))
# S = float(input("Dastlabki masofani kiriting (km): "))
# T = float(input("Harakatlanish vaqti T ni kiriting (soat): "))
# new_distance = S + (V1 + V2) * T
# print("T vaqtdan keyin ular orasidagi yangi masofa:",new_distance,"km")

# Begin37
# V1 = float(input("Birinchchi avtomobil tezligini kiriting (km/soat): "))
# V2 = float(input("Ikkinchisiniki tezligini kiriting (km/soat): "))
# S = float(input("Dastlabki masofani kiriting (km): "))
# T = float(input("Harakatlanish vaqti T ni kiriting (soat): "))
# new_distance = S - (V1 + V2) * T
# print("T vaqtdan keyin ular orasidagi yangi masofa:",new_distance,"km")

#Begin38
# A = float(input("Please enter A: "))
# B = float(input("Please enter B: "))
# X=(-1*B)/A
# print(X)

#Begin39
# A = float(input("Please enter A: "))
# B = float(input("Please enter B: "))
# C = float(input("Please enter C: "))

# D = B**2 - 4 * A * C

# if D > 0:
#     x1 = (-B + math.sqrt(D)) / (2 * A)
#     x2 = (-B - math.sqrt(D)) / (2 * A)
#     print('x1 =',x1,'x2=',x2)
# elif D == 0:
#     x1 = -B / (2 * A)
#     print('x1 and x2 =',x1)
# else:
#     print("There are no real roots")

# Begin40
# A1= float(input("Please enter A1 "))
# B1= float(input("Please enter B1 "))
# C1= float(input("Please enter C1 "))
# A2= float(input("Please enter A2 "))
# B2= float(input("Please enter B2 "))
# C2= float(input("Please enter C2 "))
# D=(A1*B2-A2*B1)
# x=(C1*B2-C2*B1)/D
# y=(C2*A1-A2*C1)/D
# print('x=',x,'y=',y)