c=input("nap vao 1 ky tu ")
if len(c)!=1:
    print("nhap lai ")
else:
        if c.isalpha():
              print(f"{c} là kí tu alphabet")
        else:
              print(f"{c} không phải là kí tự alphabet")