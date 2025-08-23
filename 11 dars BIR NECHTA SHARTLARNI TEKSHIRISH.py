"""
17-AVGUST 2025-YIL
PYTHON DARSLARI
11 dars BIR NECHTA SHARTLARNI TEKSHIRISH
OTABEK NURALIYEV
"""

#Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son 
#kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.

juft_son=int(input("Juft son kiting:\n>>>"))
qoldiq=juft_son%2
if qoldiq==0:
    print("Rahmat!")
else:
    print("Bu juft son emas")

2
#Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
#Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
#Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
#Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

foydalanuvchi_yoshi=int(input("Yoshingizni kiriting\n>>>"))
if foydalanuvchi_yoshi<4:
    narx=0
elif foydalanuvchi_yoshi>60:
    narx=0
elif foydalanuvchi_yoshi<18:
    narx=10000
elif foydalanuvchi_yoshi>=18:
    narx=20000
if narx==0:
    print(f"Sizga kirish bepul!")
else:
    print(f"Sizga kirish {narx} ming so'm")

birinchi_son=int(input("Birinchi sonni kiriting:"))
ikkinchi_son=int(input("Ikkinchi sonni kiriting:"))
if birinchi_son>ikkinchi_son:
    print(f"{birinchi_son}>{ikkinchi_son}")
elif birinchi_son==ikkinchi_son:
    print(f"{birinchi_son}={ikkinchi_son}")
elif birinchi_son<ikkinchi_son:
    print(f"{birinchi_son}<{ikkinchi_son}")

#mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
#Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 
#5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati 
#bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" 
#aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

mahsulotlar=["non", "kartoshka", "sabzi", "piyoz", "pomidor", "quruq meva", "qurut", "xolva", "kolbasa", "cola"]
savat=[]
for n in range(5):
    savat.append(input(f"{n+1}-mahsulot nomini kiriting>>>"))
for savatdagi_mahsulot in savat:
    if savatdagi_mahsulot.lower() in mahsulotlar:
        print(f"{savatdagi_mahsulot} ✅")
    else:
        print(f"{savatdagi_mahsulot} ❌")

mahsulotlar=["non", "kartoshka", "sabzi", "piyoz", "pomidor", "quruq meva", "qurut", "xolva", "kolbasa", "cola"]
bor_mahsulotlar=[]
mavjud_emas=[]
for n in range(5):
   soralgan_mahsulot=input(f"{n+1}-mahsulot nomini kiriting:\n>>>")
   if soralgan_mahsulot in mahsulotlar:
      bor_mahsulotlar.append(soralgan_mahsulot)
   else:
    mavjud_emas.append(soralgan_mahsulot)
if mavjud_emas:#roýxat bo'sh bo'lmasa
   print("Do'konimizda quyidagi mahsulotlar yo'q:")
   for yoq_mahsulot in mavjud_emas:
       print(f"- {yoq_mahsulot}")
else:
    print("Barcha so'ralgan mahsulotlar do'konimizda bor ✅")

#foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
#Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan 
#loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar 
#ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks 
#holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

foydalanuvchilar=["eshmat", "toshmat", "g'ishmat", "falonchi", "pistonchi"]
foydalanuvchi_nomi=input("Yangi logini kiriting: ").lower()
if foydalanuvchi_nomi in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz {foydalanuvchi_nomi.title()}!")

#Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan 
#sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring.

son=int(input("Ixtiyoriy son kiriting: "))
for boluvchi in range(9):
    if son%(boluvchi+2)==0:
        print(f"{son} soni {boluvchi+2} ga qoldiqsiz bo'linadi")