Movie = namedtuple("Movie",["title","rating","year"])
movia=[("Solo leviling",9,2024),
       ("Naruto",9,1994),
       ("Jahhanam Jannati 2",8,2026),
       ("jodugarlar Jangi",5,2025),
       ("Qaxramon bolish X",5,2005)]
for i in movia:
    st4=Movie(*i)
    if st4.year > 2015 and st4.rating >=8:
        print(f"{st4.title} - {st4.rating} - {st4.year}")
