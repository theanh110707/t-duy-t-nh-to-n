a=input("nhap vao: ")
if len(a)!=1:
    print("nhap lai")
else:
    if a.isalpha:
        print("la chu cai")
    elif a.isdigit:
        print("la chu so")
    else:
        print(" khong hop le")            