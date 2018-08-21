# yob = int(input("Your year of birth? "))
# age = 2018 - yob
# print("Your age:", age)

# if age < 10:
#     print("Baby")
# elif age < 18:
#     print("Teenager")
# else:
#     print("Adult")  

print("Hay dien cac tham so a, b, c trong phuong trinh bac 2: ax2 + bx + c = 0")
a = float(input("a: "))         
b = float(input("b: "))
c = float(input("c: "))

delta = b**2 - 4*a*c
delta_sqrt = delta*0.5
a_2 = 2*a

if a == 0:
    x = -c / b
    print("Phuong trinh co 1 nghiem:", x)
elif delta > 0:
    x1 = (-b + delta_sqrt) / a_2
    x2 = (-b - delta_sqrt) / a_2
    print("Phuong trinh co 2 nghiem phan biet:","x1 =",x1,"x2 =", x2)
elif delta == 0:
    x = -b / a_2
    print("Phuong trinh co 1 nghiem duy nhat x =", x)
else:
    print("Phuong trinh vo nghiem")
