"""
3-AVGUST 2025-YIL
PYTHON DARSLARI
07 dars LIST (RO'YXAT))
OTABEK NURALIYEV
"""
"""
ismlar=["Sardor", "Inoyatillo", "Jasurbek", "Sevinchbek", "Umdjon", "Sanjar"]
print(ismlar[0], "bugun futbolga boramizmi?")
print("Assalomu alaykum!" ,ismlar[1], "do'stim telefoningni ko'tar.")
print(ismlar[2] , "📢, qattasan!!!")
"""
"""
t_shaxslar = ["Amir Temur", "Ibn Sino", "Alisher Navoiy", "Ulug'bek", "Ahmad Yassaviy", 
              "Beruniy", "Jaloliddin Manguberdi", "Zahiriddin Muhammad Bobur", "Socrates", "Leonardo da Vinci"]

z_shaxslar = ["Elon Musk", "Malala Yousafzai", "Cristiano Ronaldo", "Bill Gates", "Barack Obama", 
              "Emma Watson", "Mark Zuckerberg", "Greta Thunberg", "Usain Bolt", "Abiy Ahmed"]
print('Men tarixiy shaxslardan ', t_shaxslar[-1], ", zamonaviy shaxslardan esa ", z_shaxslar[0], "bilan suhbat qilishni istar edim.")
"""

friends=[]
friends.append("Jalol")
friends.append("Kamol")
friends.append("Fazliddin")
friends.append("Asilbek")
friends.append("Javohir")
friends.append("In'omjon")
print(friends)

#Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friends.remove("Fazliddin")
friends.remove("Asilbek")
friends.remove("Javohir")
print(friends)

#Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
royxat_boshi=0
royxat_ortasi=int(round(len(friends)/2)+1)
royxat_oxiri=int(len(friends)+2)
friends.insert(royxat_boshi, "A'zamxon")
friends.insert(royxat_ortasi, "Eshturdi")
friends.insert(royxat_oxiri, "Toshturdi")
print(friends)

#Yangi mehmonlardeb nomlangan bo'sh ro'yxat yarating. .pop() va .append() 
#metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends 
#ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar=[]
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-2))
print(mehmonlar)
print(friends)