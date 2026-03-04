ten_chu_ho=str(input("Ten chu ho: "))
so_dien_thang_truoc=int(input("chi so thang truoc: "))
so_dien_thang_nay=int(input("chi so thang nay: "))
chi_so=so_dien_thang_nay-so_dien_thang_truoc
if chi_so <=50:
    tien_dien=chi_so*1984
elif chi_so <=100:
    tien_dien= 50*1984+(chi_so-50)*2050
elif chi_so <=200:
     tien_dien= 50*1984+50*2050 +(chi_so-100)*2380
elif chi_so <=300:
     tien_dien= 50*1984+50*2050 +100*2380+(chi_so-200)*2998
elif chi_so <=400:
     tien_dien= 50*1984+50*2050 +100*2380+100*2998+(chi_so-300)*3350
else:
     tien_dien=50*1984+50*2050 +100*2380+100*2998+100*3350+(chi_so-400)*3460



tien=round(tien_dien+tien_dien*0.08)
print(f"Ho va ten: {ten_chu_ho}")
print(f"Tien phai tra la: {tien}")
