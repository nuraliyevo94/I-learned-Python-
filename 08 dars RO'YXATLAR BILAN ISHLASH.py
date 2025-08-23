"""
8-AVGUST 2025-YIL
PYTHON DARSLARI
08 dars LIST (RO'YXAT))
OTABEK NURALIYEV
"""
#O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar=["oʻzbekiston", "qozogʻiston", "tojikiston", "qirgʻiziston", "turkmaniston", "rossiya", "xitoy", "hindiston", "pokiston", "afgʻoniston", "turkiya", "eron", "saudiya arabistoni", "baa", "misr", "janubiy koreya", "yaponiya", "germaniya", "fransiya", "aqsh"]

#Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))

#sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))

#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))

#Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)

#reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)

#sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

#120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar=list(range(120,1201,2))
print(juft_sonlar)

#Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print("Yig'indi=", sum(juft_sonlar))

#Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print("Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring:",max(juft_sonlar)-min(juft_sonlar))

#Ro'yxatdagi elementlar sonini hisoblang
print("Ro'yxatdagi elementlar sonini hisoblang:", len(juft_sonlar))

#Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print("Boshidagi 20 ta son:", juft_sonlar[0:21])
a=int((len(juft_sonlar))/2-10)
b=int((len(juft_sonlar))/2+10)
print("O'rtadagi 20 ta son:", juft_sonlar[a:b])
print("oxirgi 20 ta son", juft_sonlar[521:541])

#taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar=["non", "qaymoq", "kabob", "palov", "do'lma"]

#nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta=taomlar[:]

#Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove("kabob")
nonushta.remove("palov")
nonushta.remove("do'lma")
nonushta.append("asal")
nonushta.append("tuxum")

#Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

#Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta.remove("non")
nonushta.remove("qaymoq")
nonushta.reverse()
nonushta.append("qaymoq va non")
nonushta.reverse()
print(nonushta)
print(nonushta[0])