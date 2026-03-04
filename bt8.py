nam=int(input("nhap nam "))
if nam<0:
    print("nhap lai")
else:
    if nam % 400==0 or (nam%4==0 and nam% 100!=0):
        print("nam nhuan")
    else:
        print("nam khong nhuan")    
   