nam_sinh=int(input("nhap vap nam sinh: "))
nam=int(input("nhap nam: "))
if nam_sinh>0 and nam >0:
    tuoi= nam-nam_sinh
    if tuoi>=18:
        print("Du tuoi")
    else :
        print("Chua du tuoi")
else:
    print("nhap lai")            