nam_sinh=int(input( "nhap nam sinh "))
if nam_sinh <0:
    print("nhap lai")
else:
    tuoi= 2025-nam_sinh
    if tuoi>=18:
        print("du tuoi")
    else:
        print("chua du tuoi")        