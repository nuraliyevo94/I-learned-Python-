"""
31-AVGUST 2025-YIL
PYTHON DARSLARI
16 dars NESTING
OTABEK NURALIYEV
"""

"""
# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. 
# Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

shaxslar = [
    {
        "ism": "Alisher Navoiy",
        "soha": "Adabiyot",
        "ma'lumot": "Buyuk o'zbek shoiri, mutafakkir va davlat arbobi. 'Xamsa' asarlari muallifi.",
        "t_yil": 1441,
        "viloyat": "Hirot (Xuroson)",
        "yashagan": "60 yil (1441–1501) umr ko'rgan"
    },
    {
        "ism": "Abu Ali ibn Sino",
        "soha": "Ilm-fan (tibbiyot, falsafa)",
        "ma'lumot": "'Tib qonunlari' asari muallifi, Sharq allomasi, buyuk tabib.",
        "t_yil": 980,
        "viloyat": "Buxoro (Afshona qishlog'i)",
        "yashagan": "57 yil (980–1037) umr ko'rgan"
    },
    {
        "ism": "Abu Rayhon Beruniy",
        "soha": "Ilm-fan (astronomiya, geografiya, tarix)",
        "ma'lumot": "Buyuk qomusiy olim, 'Qadimgi xalqlardan qolgan yodgorliklar' asari muallifi.",
        "t_yil": 973,
        "viloyat": "Xorazm",
        "yashagan": "75 yil (973–1048) umr ko'rgan"
    },
    {
        "ism": "William Shakespeare",
        "soha": "Adabiyot (dramaturgiya)",
        "ma'lumot": "Ingliz dramaturgi va shoiri, 'Hamlet', 'Romeo va Julietta' asarlari muallifi.",
        "t_yil": 1564,
        "viloyat": "Angliya (Stratford-upon-Avon)",
        "yashagan": "52 yil (1564–1616) umr ko'rgan"
    },
    {
        "ism": "Albert Einstein",
        "soha": "Ilm-fan (fizika)",
        "ma'lumot": "Nisbiylik nazariyasi asoschisi, Nobel mukofoti sovrindori.",
        "t_yil": 1879,
        "viloyat": "Germaniya (Ulm shahri)",
        "yashagan": "76 yil (1879–1955) umr ko'rgan"
    },
    {
        "ism": "Leonardo da Vinci",
        "soha": "San'at, ilm-fan",
        "ma'lumot": "Renessans davrining dahosi, rassom, ixtirochi. 'Mona Liza' asari muallifi.",
        "t_yil": 1452,
        "viloyat": "Italiya (Vinci shahri)",
        "yashagan": "67 yil (1452–1519) umr ko'rgan"
    },
    {
        "ism": "Abdurauf Fitrat",
        "soha": "Adabiyot, jadidchilik",
        "ma'lumot": "Jadid adibi va olimi, ma'rifatparvar, 'Oila' risolasi muallifi.",
        "t_yil": 1886,
        "viloyat": "Buxoro",
        "yashagan": "53 yil (1886–1939) umr ko'rgan"
    },
    {
        "ism": "Steve Jobs",
        "soha": "Internet, texnologiya",
        "ma'lumot": "Apple kompaniyasi asoschisi, zamonaviy texnologiyalar rivojiga katta hissa qo'shgan.",
        "t_yil": 1955,
        "viloyat": "AQSh (San-Fransisko)",
        "yashagan": "56 yil (1955–2011) umr ko'rgan"
    },
    {
        "ism": "Elon Musk",
        "soha": "Internet, texnologiya, kosmonavtika",
        "ma'lumot": "SpaceX va Tesla asoschisi, zamonaviy innovatsion texnologiyalar yetakchisi.",
        "t_yil": 1971,
        "viloyat": "Janubiy Afrika (Pretoria)",
        "yashagan": "Hozirda yashab kelmoqda"
    },
    {
        "ism": "Mark Zuckerberg",
        "soha": "Internet",
        "ma'lumot": "Facebook (Meta) asoschisi, ijtimoiy tarmoqlar rivojiga hissa qo'shgan.",
        "t_yil": 1984,
        "viloyat": "AQSh (Nyu-York)",
        "yashagan": "Hozirda yashab kelmoqda"
    }
]
for shaxs in shaxslar:
    print(f"{shaxs['ism'].title()} {shaxs['t_yil']}-yilda {shaxs['viloyat'].title()}da tug'ilgan.\n"
          f"{shaxs['yashagan']}. {shaxs['soha']} soha(lari)da ishlagan (ishlaydi). \n{shaxs["ma'lumot"]}\n")



# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
# For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

adabiyot = [
    {
        "ism": "Alisher Navoiy",
        "davr": "1441–1501",
        "mamlakat": "Xuroson",
        "asarlari": ["Xamsa", "Lison ut-Tayr", "Muhokamat ul-lug‘atayn", "Mahbub ul-qulub", "Mezon ul-avzon"]
    },
    {
        "ism": "Abdurauf Fitrat",
        "davr": "1886–1939",
        "mamlakat": "O‘zbekiston (Buxoro)",
        "asarlari": ["Oila", "Chin sevish", "Sayha", "Munozara", "Hind ixtilolchilari"]
    },
    {
        "ism": "Abdulla Qodiriy",
        "davr": "1894–1938",
        "mamlakat": "O‘zbekiston",
        "asarlari": ["O‘tkan kunlar", "Mehrobdan chayon", "Obid ketmon", "Kalvak Mahzum", "Juvonboz"]
    },
    {
        "ism": "Cho‘lpon (Abdulhamid Sulaymon o‘g‘li)",
        "davr": "1897–1938",
        "mamlakat": "O‘zbekiston",
        "asarlari": ["Kecha va kunduz", "Buloqlar", "Uyg‘onish", "Turon qo‘shig‘i", "Go‘zal Turkiston"]
    },
    {
        "ism": "Erkin Vohidov",
        "davr": "1936–2016",
        "mamlakat": "O‘zbekiston",
        "asarlari": ["Tong nafasi", "Yoshlik devoni", "Ruhlar isyoni", "O‘zbegim", "Nido"]
    },
    {
        "ism": "G‘afur G‘ulom",
        "davr": "1903–1966",
        "mamlakat": "O‘zbekiston",
        "asarlari": ["Shum bola", "Netay", "Sen yetim emassan", "Yodgor", "Mening o‘zbekistonim"]
    },
    {
        "ism": "William Shakespeare",
        "davr": "1564–1616",
        "mamlakat": "Angliya",
        "asarlari": ["Hamlet", "Romeo va Julietta", "Otello", "Qirol Lir", "Makbet"]
    },
    {
        "ism": "Fyodor Dostoyevskiy",
        "davr": "1821–1881",
        "mamlakat": "Rossiya",
        "asarlari": ["Jinoyat va jazo", "Karamazovlar", "Telba", "Qo‘rqinchli tush", "O‘lik uy xotiralari"]
    },
    {
        "ism": "Lev Tolstoy",
        "davr": "1828–1910",
        "mamlakat": "Rossiya",
        "asarlari": ["Urush va tinchlik", "Anna Karenina", "Dirijyor Kreytser sonatasi", "Bolalik", "Qozonlik asarlari"]
    },
    {
        "ism": "Abu Abdulla Rudakiy",
        "davr": "858–941",
        "mamlakat": "Tojikiston",
        "asarlari": ["Ona tilim", "Bo‘ston", "Yusuf va Zulayho", "Ko‘z yoshlarim", "Qasida"]
    }
]

for adabiyotshunos in adabiyot:
    print(f"{adabiyotshunos["ism"].title()} {adabiyotshunos['davr']}-yillarda yashab ijod qilgan. Vatani {adabiyotshunos['mamlakat'].title()}.")
    print(f"Mashhur asarlari:")
    for asar in adabiyotshunos['asarlari']:
        print(f"{asar}")
    print()

# Do'stlarning sevimli kino/seriallari
sevimli_kino = {
    "Ali": ["Titanic", "Interstellar", "Harry Potter"],
    "Vali": ["Avengers", "Sherlock Holmes", "Spider-Man"],
    "G'ani": ["Ertug'rul", "Prison Break", "Breaking Bad"]
}

for ism, kinolar in sevimli_kino.items():
    print(f"\n{ism}ning sevimli kino/seriallari:")
    for kino in kinolar:
        print(f" - {kino}")
        

# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. 
# Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    "o'zbekiston": {
        "poytaxt": "Toshkent",
        "maydon": 448978,   # km²
        "aholi": 36000000,
        "til": "o'zbek tili"
    },
    "aqsh": {
        "poytaxt": "Vashington",
        "maydon": 9833517,
        "aholi": 331000000,
        "til": "ingliz tili"
    },
    "rossiya": {
        "poytaxt": "Moskva",
        "maydon": 17098246,
        "aholi": 146000000,
        "til": "rus tili"
    },
    "yaponiya": {
        "poytaxt": "Tokio",
        "maydon": 377975,
        "aholi": 125800000,
        "til": "yapon tili"
    }
}


for davlat, info in davlatlar.items():
    print(f"\n{davlat.title()} davlati haqida ma'lumot:")
    print(f" Poytaxti: {info['poytaxt']}")
    print(f" Maydoni: {info['maydon']} km²")
    print(f" Aholisi: {info['aholi']} kishi")
    print(f" Davlat tili: {info['til']}")

"""
# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan 
# davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat 
# haqida ma'lumot yo'q" degan xabarni chiqaring (Men ko'proq davlat kiritdim).

davlatlar = {
    "o'zbekiston": {
        "poytaxt": "Toshkent",
        "maydon": 448978,
        "aholi": 36000000,
        "til": "o'zbek tili"
    },
    "aqsh": {
        "poytaxt": "Vashington",
        "maydon": 9833517,
        "aholi": 331000000,
        "til": "ingliz tili"
    },
    "rossiya": {
        "poytaxt": "Moskva",
        "maydon": 17098246,
        "aholi": 146000000,
        "til": "rus tili"
    },
    "xitoy": {
        "poytaxt": "Pekin",
        "maydon": 9596961,
        "aholi": 1410000000,
        "til": "xitoy tili (mandarin)"
    },
    "hindiston": {
        "poytaxt": "Yangi Dehli",
        "maydon": 3287263,
        "aholi": 1380000000,
        "til": "hind va ingliz tillari"
    },
    "yaponiya": {
        "poytaxt": "Tokio",
        "maydon": 377975,
        "aholi": 125800000,
        "til": "yapon tili"
    },
    "germaniya": {
        "poytaxt": "Berlin",
        "maydon": 357022,
        "aholi": 83000000,
        "til": "nemis tili"
    },
    "fransiya": {
        "poytaxt": "Parij",
        "maydon": 551695,
        "aholi": 67000000,
        "til": "fransuz tili"
    },
    "buyuk britaniya": {
        "poytaxt": "London",
        "maydon": 243610,
        "aholi": 67000000,
        "til": "ingliz tili"
    },
    "italiya": {
        "poytaxt": "Rim",
        "maydon": 301340,
        "aholi": 60000000,
        "til": "italyan tili"
    },
    "ispaniya": {
        "poytaxt": "Madrid",
        "maydon": 505990,
        "aholi": 47000000,
        "til": "ispan tili"
    },
    "turkiya": {
        "poytaxt": "Anqara",
        "maydon": 783356,
        "aholi": 85000000,
        "til": "turk tili"
    },
    "qozog'iston": {
        "poytaxt": "Ostonа",
        "maydon": 2724900,
        "aholi": 19000000,
        "til": "qozog' va rus tillari"
    },
    "qirg'iziston": {
        "poytaxt": "Bishkek",
        "maydon": 199951,
        "aholi": 6600000,
        "til": "qirg'iz va rus tillari"
    },
    "tojikiston": {
        "poytaxt": "Dushanbe",
        "maydon": 143100,
        "aholi": 9500000,
        "til": "tojik tili"
    },
    "afg'oniston": {
        "poytaxt": "Kobul",
        "maydon": 652230,
        "aholi": 38900000,
        "til": "dari va pushtu tillari"
    },
    "misr": {
        "poytaxt": "Qohira",
        "maydon": 1002450,
        "aholi": 104000000,
        "til": "arab tili"
    },
    "braziliya": {
        "poytaxt": "Brazilia",
        "maydon": 8515767,
        "aholi": 212000000,
        "til": "portugal tili"
    },
    "kanada": {
        "poytaxt": "Ottava",
        "maydon": 9984670,
        "aholi": 38000000,
        "til": "ingliz va fransuz tillari"
    },
    "avstraliya": {
        "poytaxt": "Kanberra",
        "maydon": 7692024,
        "aholi": 26000000,
        "til": "ingliz tili"
    }
}

davlat=input("Ma'lumot olmoqchi bo'lgan davlat nomini kiriting\n>>>").lower()
if davlat in davlatlar:   # faqat kalitlarni tekshiradi
    info = davlatlar[davlat]   # shu joyda info lug'atga tenglashadi
    print(f"\n{davlat.title()} davlati haqida ma'lumot:")
    print(f" Poytaxti: {info['poytaxt']}")
    print(f" Maydoni: {info['maydon']} km²")
    print(f" Aholisi: {info['aholi']} kishi")
    print(f" Davlat tili: {info['til']}")
else:
    print("Kechirasiz, bu davlat haqida ma'lumot topilmadi.")