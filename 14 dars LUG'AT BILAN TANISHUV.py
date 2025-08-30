"""
30-AVGUST 2025-YIL
PYTHON DARSLARI
14 dars LUG'AT BILAN TANISHUV
OTABEK NURALIYEV
"""

"""
#otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson 
#haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo).
#Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yil

ukam_0={"ism":"G'iyos", "yosh":21, "ish_joyi":"O'zbekiston-Finlandiya pedogogika intituti"}
print(f"Mening ukam {ukam_0["ism"].title()} {ukam_0["yosh"]} yoshda va u {ukam_0["ish_joyi"]}da o'qiydi (ishlaydi).")


python_lugat = {
    "integer": "Butun son (masalan: -5, 0, 42)",
    "float": "O'nlik son (masalan: 3.14, -0.5)",
    "string": "Matn ifodasi (masalan: 'salom', \"python\")",
    "boolean": "Mantiqiy qiymat: True (rost) yoki False (yolg'on)",
    "list": "Ro'yxat, bir nechta elementlar to'plami (masalan: [1, 2, 3])",
    "tuple": "O'zgarmas ro'yxat (masalan: (1, 2, 3))",
    "dictionary": "Kalit-qiymat juftligi saqlovchi tuzilma (masalan: {\"ism\": \"Ali\"})",
    "if": "Shart operatori, kodni shartga qarab bajaradi",
    "else": "Shart bajarilmasa, boshqa blokni bajaradi",
    "for": "Takrorlash operatori, ketma-ket elementlarni aylanib chiqadi"
}




#Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
#Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

sevimli_taom = {
    "oyim":"Sho'rva, pichak, do'lma",
    "dadam":"Lag'mon, manti, do'lma",
    "ukam":"Kalla sho'rva, shashlik, palov"}
shaxs = input("Shaxsni kiriting:\n>>> ").lower()
print(sevimli_taom[shaxs])




#Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. 
#Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

en_uz = {
    "milk":"sut",
    "sugar":"shakar",
    "grape":"uzum",
    "bread":"non",
    "donkey":"eshak",
    "monkey":"maymun",
    "sightseeing":"diqqatga sazovor joyni tomosha qilish",
    "i":"men",
    "go":"bormoq",
    "flow":"esmoq"
    }
soz = input("Qaysi so'zning tarjimasini topamiz\n>>>")
tarjima = en_uz.get(soz, "Afsuski, bu so'z lug'atimizda yo'q ekan, boshqa manbadan foydalanib ko'ring.")
print(tarjima)


"""


#Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.

en_uz = {
    "milk": "sut",
    "sugar": "shakar",
    "grape": "uzum",
    "bread": "non",
    "donkey": "eshak",
    "monkey": "maymun",
    "sightseeing": "diqqatga sazovor joyni tomosha qilish",
    "i": "men",
    "go": "bormoq",
    "flow": "esmoq"
}

soz = input("Qaysi so'zning tarjimasini topamiz?\n>>> ").lower()

if soz in en_uz:
    print(f"'{soz}' so'zining tarjimasi: {en_uz[soz]}")
else:
    print(f"Afsuski, '{soz}' so'zi lug'atimizda yo'q ekan. Boshqa manbadan foydalanib ko'ring.")
