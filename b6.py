import math

a= int(input("nhap vao canh a: "))
b= int(input("nhap vao canh b: "))
c= int(input("nhap vao canh c: "))
if (a+b>c) and (a+c>b) and (b+c>a):
    p=(a+b+c)/2
    dien_tich_tam_giac=round(math.sqrt(p*(p-a)*(p-b)*(p-c)),1)
    print(f"dien tich tam giac la: {dien_tich_tam_giac}")
else:
    print("khong phai 3 canh tam giac")    
