c=str(input())
if len(c) !=1:
    print("nhap lai ky tu")
else:
    
    if c.isupper():
        ket_qua = c.lower()
        print(f"chu thuong la: {ket_qua}")
    elif c.islower():
        ket_qua = c.upper()
        print(f"chu hoa la: {ket_qua}")
    