a= int(input("nhap diem "))
if a<0:
    print("nhap lai diem ")
elif 0<=a<=10:
    if a>=8:
        print("gioi")
    elif 6.5<=a<8:
        print("kha")
    elif 5<=a<6.5:
        print("trung bình")
    else:
        print("yeu")
else:
    print("nhap lai")        
