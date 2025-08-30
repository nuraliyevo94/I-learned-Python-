"""
30-AVGUST 2025-YIL
PYTHON DARSLARI
15 dars LUG'AT ELEMENTLARI BILAN ISHLASH
OTABEK NURALIYEV
"""

"""
#Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
#Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo 
#ketma-ketligida chiroyli qilib konsolga chiqaring. 

python_lugat = {
    "integer": "Butun son (masalan: -5, 0, 42)",
    "float": "O'nlik son (masalan: 3.14, -0.5)",
    "string": "Matn ifodasi (masalan: 'salom', \"python\")",
    "boolean": "Mantiqiy qiymat: True (rost) yoki False (yolg'on)",
    "list": "Ro'yxat, bir nechta elementlar to'plami (masalan: [1, 2, 3])",
    "tuple": "O'zgarmas ro'yxat (masalan: (1, 2, 3))",
    "dictionary": "Kalit-qiymat juftligi saqlovchi tuzilma (masalan: {\"ism\":\"Ali\"})",
    "set": "Unikal elementlar to'plami (masalan: {1, 2, 3})",
    "if": "Shart operatori, kodni shartga qarab bajaradi",
    "else": "Shart bajarilmasa, boshqa blokni bajaradi",
    "elif": "Birinchi shart bajarilmasa, boshqa shartni tekshiradi",
    "for": "Takrorlash operatori, ketma-ket elementlarni aylanib chiqadi",
    "while": "Shart bajarilguncha kodni qayta-qayta bajaradi",
    "function": "Ma'lum vazifani bajaruvchi kod bloki (def yordamida yaratiladi)",
    "class": "Obyektlar yaratish uchun shablon, OOP asosiy tushunchasi",
    "module": "Tayyor funksiyalar va kutubxonalar to'plami (masalan: math, random)",
    "import": "Tashqi modul yoki kutubxonani dasturga chaqirish uchun ishlatiladi",
    "try-except": "Xatolarni ushlab olish va dastur to'xtab qolishini oldini olish uchun ishlatiladi"
}

for kalit, izoh in python_lugat.items():
    print(f"{kalit.title()} - {izoh}")



#Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, 
#alifbo ketma-ketligida konsolga chiqaring. 

davlatlar = {
    "o'zbekiston": "toshkent",
    "qozog'iston": "nursulton",
    "qirg'iziston": "bishkek",
    "tojikiston": "dushanbe",
    "turkmaniston": "ashxobod",
    "rossiya": "moskva",
    "xitoy": "pekin",
    "yaponiya": "tokio",
    "janubiy koreya": "seul",
    "hindiston": "dehli",
    "pokiston": "islomobod",
    "afg'oniston": "qobul",
    "turkiya": "anqara",
    "aqsh": "vashington",
    "kanada": "ottava",
    "germaniya": "berlin",
    "fransiya": "parij",
    "italiya": "rim",
    "angliya": "london",
    "ispaniya": "madrid"
}

davlatlar_list = []
for davlat in davlatlar.keys():
    davlatlar_list.append(davlat)
    davlatlar_list.sort()
print(f"Davlatlar va ularning poytaxtlari:\nDAVLATLAR - POYTAXTLAR")
for davlat_royxatdan in davlatlar_list:
    print(f"{davlat_royxatdan.title()} - {davlatlar[davlat_royxatdan].title()}")



#Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. 
#Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
davlatlar = {
    "o'zbekiston": "toshkent",
    "qozog'iston": "nursulton",
    "qirg'iziston": "bishkek",
    "tojikiston": "dushanbe",
    "turkmaniston": "ashxobod",
    "rossiya": "moskva",
    "xitoy": "pekin",
    "yaponiya": "tokio",
    "janubiy koreya": "seul",
    "hindiston": "dehli",
    "pokiston": "islomobod",
    "afg'oniston": "qobul",
    "turkiya": "anqara",
    "aqsh": "vashington",
    "kanada": "ottava",
    "germaniya": "berlin",
    "fransiya": "parij",
    "italiya": "rim",
    "angliya": "london",
    "ispaniya": "madrid"
}

davlat = input("Istalgan davlatnio kiriting\n>>>").lower()
poytaxt = davlatlar.get(davlat.title, "Bizda bunday ma'lumot yo'q.")
print(poytaxt)

"""

#Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
#Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom 
#yo'q" degan xabarni chiqaring.

menu = {
    "osh": 25000,
    "lag'mon": 22000,
    "manti": 20000,
    "shashlik": 18000,
    "norin": 23000,
    "sho'rva": 17000,
    "mastava": 16000,
    "dimlama": 24000,
    "somsa": 10000,
    "chuchvara": 19000,
    "qozon kabob": 26000,
    "beshbarmoq": 27000,
    "qovurma lag'mon": 24000,
    "do'lma": 21000,
    "pichak": 15000,
    "kabob": 20000,
    "fri kartoshka": 12000,
    "hamburger": 25000,
    "cheeseburger": 27000,
    "hot-dog": 15000,
    "pizza": 40000,
    "lavash": 22000,
    "shawarma": 23000,
    "tandir somsa": 12000,
    "kfc tovuq": 30000,
    "tovuq go'shti": 28000,
    "qiyma somsa": 11000,
    "baliq qovurmasi": 35000,
    "sutli choy": 5000,
    "qora choy": 4000,
    "ko'k choy": 4000,
    "coffee": 15000,
    "cola": 10000,
    "fanta": 10000,
    "suv (0.5l)": 5000
}

buyurtma_soni = int(input("Nechta taom buyurtma qilmoqchisiz?\n>>> "))

buyurtmalar = []
umumiy_summa = 0

for n in range(buyurtma_soni):
    taom = input(f"{n+1}-taom nomini kiriting:\n>>> ").lower()
    if taom in menu:
        buyurtmalar.append((taom, menu[taom]))  # (taom, narh) qo'shamiz
        umumiy_summa += menu[taom]
    else:
        buyurtmalar.append((taom, None))  # taom topilmasa None

# Natija chiqarish
print("\n🍽 Buyurtmalar ro'yxati:")
for taom, narh in buyurtmalar:
    if narh:
        print(f"✅ {taom.title()} - {narh} so'm")
    else:
        print(f"❌ {taom.title()} bizda yo'q ekan.")

print(f"\n💰 Umumiy hisob: {umumiy_summa} so'm")

