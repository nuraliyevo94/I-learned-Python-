"""
8-AVGUST 2025-YIL
PYTHON DARSLARI
09 dars FOR TAKRORLASH OPERATORI
OTABEK NURALIYEV
"""

#Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir 
#ismga takrorlanuvchi xabar yozing
ismlar=["Eshturdi", "Toshturdi", "Moshkichri", "G'alcha", "Falonchi", "Pistonchi"]
for ism in ismlar:
    print("Salom", ism, "! Sen bu yerda nima qilyapsan?")
    
#Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan 
#xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
print(f"Kod {len(ismlar)} marta takrorlandi.")

#10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir
#elementining kubini yangi qatordan konsolga chiqaring.
toq_sonlar=list(range(11,100,2))
for toq_son in toq_sonlar:
    print(f"{toq_son} ning kubi {toq_son**3} ga teng\n")

#Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar
#degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
kinolar=[]
print("Ozingiz yoqtirgan 5 ta kinofilm nomini kiriting")
for n in range(5):
    kinolar.append(input(f"{n+1}-film nomini kiriting:"))
print(kinolar)

suhbatdoshlar=[]
m=int(input("Bugun necha kishi bilan suhbatlashdingiz?\n>>>"))
for s in range(m):
    suhbatdoshlar.append(input(f"{s+1}-suhbatdoshingiz ismini kiriting\n>>>"))
print(suhbatdoshlar)