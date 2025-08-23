"""
12-AVGUST 2025-YIL
PYTHON DARSLARI
10 dars IF-ELSE
OTABEK NURALIYEV
"""

#Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat 
#elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni
#katta qiling.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
#    if car=='gm':
#       print(car.upper())
#    else:
#        print(car.title())


#Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
    if car!='gm':
        print(car.title())
    else:
        print(car.upper())
        
#Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, 
#"Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini 
#konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini 
#konsolga chiqaring.
ism=input("Ismingizni kiriting\n>>>")
ism.lower()
if ism=="otabek":
    print("Xush kelibsiz, Otabek. Foydalanuvchilar ro'yxatini ko'rasizmi?")
else:
    ism=ism.title()
    print(f"Xush kelibsiz {ism}!")
#Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, 
#"Sonlar teng" ekan degan yozuvni konsolga chiqaring.
birinchi_son=float(input("Birinchi sonni kiriting/n>>>"))
ikkinchi_son=float(input("Ikkinchi sonni kiriting/n>>>"))
if birinchi_son==ikkinchi_son:
    print("Sonlar teng")

#Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga 
#"Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring. 
son=float(input("Ixtiyoriy son kiriting\n>>>"))
if son>=0:
    print("Musbat son")
if son==0:
    print("0 (nol) soni musbat son ham, manfiy son ham hisoblanmaydi")
else:
    print("Manfiy son")

#Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini
#hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, 
#"Musbat son kiriting" degan xabarni chiqaring. 
son2=float(input("Ixtiyoriy son kiriting\n>>>"))
if son2<0:
    print("Manfiy sonni kvadrat ildizini hisoblash mumkin emas")
if son2>=0:
    kv_ildiz=son2**0.5
    print(kv_ildiz)