from collections import namedtuple
from datetime import datetime
#1
# Studenst = namedtuple('Student', ['name','age', 'score'])

# student = [
#     ('Ali', 20, 85),
#     ('Eshmat', 22, 78),
#     ('Vali', 19, 90),
#     ('Hoshim', 21, 88)
# ]

# for student in student:
#     st = Studenst(*student)
#     if st.score > 80:
#         print(st.name, st.age, st.score)




#2
# Product = namedtuple('Product', ['name', 'price', 'quantity'])

# products = [
#     ('Laptop', 30000, 5),
#     ('Smartphone', 15000, 10),
#     ('Tablet', 10000, 7),
#     ('Headphones', 150, 15)
# ]

# for product in products:
#     pr = Product(*product)
#     if pr.price * pr.quantity > 100000:
#         print(pr.name, pr.price, pr.quantity)




#3
# Person  = namedtuple('Person', ['first_name', 'last_name', 'birth_year'])
# person = [
#     ('John', 'Doe', 1990),
#     ('Jane', 'Smith', 1985),
#     ('Alice', 'Johnson', 2000),
#     ('Bob', 'Brown', 1975)
# ]
# maxs = 0
# pers = None
# for i in person:
#     st2=Person(*i)
#     year = datetime.now().year
#     age = year - st2.birth_year
#     if age > maxs:
#         maxs = age
#         pers = st2
# print(f"{pers.first_name}  {pers.birth_year}  {maxs} ")




#4
# Flight = namedtuple("Flight",["from_city","to_city","duration"])
# fligt=[
#     ("Fargona","Andijon",3),
#     ("Samarqand","AQSH",12),
#     ("Toshkent","Moskva",6),
#     ("Fargona","Toshkent",1)
# ]
# for i in fligt:
#     st3=Flight(*i)
#     if st3.duration > 2:
#         print(f"{st3.from_city}-{st3.to_city} - {st3.duration}")





#5
# Movie = namedtuple("Movie",["title","rating","year"])
# movia=[("Social network",9,2024),
#        ("Harry Potter",9,1994),
#        ("Avangards",8,2026),
#        ("Squid game",5,2025),
#        ("Spider Man",5,2005)]
# for i in movia:
#     st4=Movie(*i)
#     if st4.year > 2015 and st4.rating >=8:
#         print(f"{st4.title} - {st4.rating} - {st4.year}")





#6
# Numbers=[10,3,55,45,78,99,76,65,9,1]
# mins = min(Numbers)
# maxs = max(Numbers)
# orta = sum(Numbers)/len(Numbers)
# print(f"kichkinasi - {mins}\nkattasi - {maxs}\nortancha - {orta}")




#7
# Colors = ("red", "green", "blue", "yellow")
# print(f"blue indexsi - {Colors.index('blue')}")
# colors_l = list(Colors)
# colors_l.append("black")
# colors = tuple(colors_l)
# print(colors)





#8
# Text = "Python 3 Ali 5 Jasur 8 Meni ismim Husanboy yoshim 17 ta "
# harf = []
# raqam = []
# bosh_joy = []
# for i in Text:
#     if i.isalpha():
#         harf.append(i)
#     elif i.isdigit():
#         raqam.append(i)
#     elif i.isspace():
#         bosh_joy.append(i)
# print(f"Harflar - {len(harf)}\nRaqamlar - {len(raqam)}\nBosh joylar - {len(bosh_joy)}")

# result = list(filter(lambda x: x // 5 * 5 == x and x // 3 * 3 != x, range(1,151)))
# print(result)






#9
#Uzur domla buni qila olmadim






#10
# Book = namedtuple("Book",["title","author","pages"])
# book=[("Harry Potter","J.K. Roulin",500),
#       ("Gravity Fals","A. Device",320),
#       ("The four","K. Alberto",160,),
#       ("Grocking algoritms","D. Antony",480),
#       ("Futbol","Cristiano Ronaldo",5000)]
# books = []
# for i in book:
#     books.append(Book(*i))
# maxs = 0
# max_pages = None
# for i in books:
#     if i.pages > maxs:
#         maxs = i.pages
#         max_pages = i
# total_pages = 0
# for i in books:
#     total_pages += i.pages
# print(f"Name: {max_pages.title}, Title:{max_pages.pages}, All:{total_pages}")

#