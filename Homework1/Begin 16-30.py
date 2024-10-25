import math
#Begin16
# x1= int(input("Please enter x1 "))
# x2= int(input("Please enter x2 "))
# distance=abs(x2-x1)
# print('distance=',distance)
#Begin17
# A= int(input("Please enter A "))
# B= int(input("Please enter B "))
# C= int(input("Please enter C "))
# d1=abs(C-A)
# d2=abs(C-B)
# d3=abs(B-A)
# distance=d1+d2+d3
# print('AC dis=',d1,'BC dis=',d2,'distance=',distance)

#Begin18
# A= int(input("Please enter A "))
# B= int(input("Please enter B "))
# C= int(input("Please enter C(must be less than b and more than a) "))
# AC=abs(C-A)
# BC=abs(B-C)
# ans=AC*BC
# print('product of ac dis and bc dis is ',ans)

#Begin19
# x1= int(input("Please enter x1 "))
# y1= int(input("Please enter y1 "))
# x2= int(input("Please enter x2 "))
# y2= int(input("Please enter y2 "))

# length = abs(x2 - x1)
# width = abs(y2 - y1)

# perimeter = 2 * (length + width)
# area = length * width

# print("Perimetri: ",perimeter)
# print("Yuzasi: ", area)

#Begin20
# x1= int(input("Please enter x1 "))
# y1= int(input("Please enter y1 "))
# x2= int(input("Please enter x2 "))
# y2= int(input("Please enter y2 "))
# distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
# print('distance= ',distance)

#Begin21
# x1= float(input("Please enter x1 "))
# y1= float(input("Please enter y1 "))
# x2= float(input("Please enter x2 "))
# y2= float(input("Please enter y2 "))
# x3= float(input("Please enter x3 "))
# y3= float(input("Please enter y3 "))
# a=math.sqrt((x2-x1)**2+(y2-y1)**2)
# b=math.sqrt((x3-x2)**2+(y3-y2)**2)
# c=math.sqrt((x3-x1)**2+(y3-y1)**2)
# p=(a+b+c)/2
# S=float(math.sqrt(p*(p-a)*(p-b)*(p-c)))
# print('perimetr= ',p,'area= ',S)

#Begin22
# a= int(input("Please enter a "))
# b= int(input("Please enter b "))
# a,b=b,a
# print('a=',a,'b=',b)

#Begin23
# a= int(input("Please enter a "))
# b= int(input("Please enter b "))
# c= int(input("Please enter c "))
# a,b,c=c,a,b
# print('a=',a,'b=',b,'c=',c)

#Begin24
# a= int(input("Please enter a "))
# b= int(input("Please enter b "))
# c= int(input("Please enter c "))
# a,b,c=b,c,a
# print('a=',a,'b=',b,'c=',c)

#Begin25
# x= int(input("Please enter x "))
# y=3*x**6-6*x**2-7
# print('y=',y)

#Begin26
# x= int(input("Please enter x "))
# y=4*(x-3)**6-7*(x-3)**3+2
# print('y=',y)

#Begin27
# a= int(input("Please enter a "))
# a2=a**2
# a3=a**4
# a4=a**8
# print(a2,a3,a4)

#Begin28
# a= int(input("Please enter a "))
# a2=a**2
# a3=a**3
# a4=a**5
# a5=a**10
# a6=a**15
# print(a2,a3,a4,a5,a6)

#Begin29
# alpha=float(input("Please enter alpha "))
# rad=alpha*(math.pi/180)
# print(rad)

#Begin30
# alpha=float(input("Please enter alpha "))
# degree=alpha*(180/math.pi)
# print(degree)