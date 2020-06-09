squares = []
for i in range(1, 101):
    squares.append(i ** 2)
print(squares)

squares2 = [i ** 2 for i in range(1, 101)]
print(squares2)

remainders5 = [x ** 2 % 5 for x in range(1, 101)]
print(remainders5)

remainders11 = [x ** 2 % 11 for x in range(1, 101)]
print(remainders11)

movies = ['bbeh (1997)',
          'Gabriel (1976 & 2007)',
          'abriel Over the White House (1933)',
          'Gabrielle: (1954, 2005 & 2013)',
          'Gaby (1956)',
          'ada Meilin (2002)',
          'Gagamboy (2004)',
          'Galaxina (1980)',
          'Galaxy Invader (1985)',
          'The Galaxy on Earth (2014), alaxy Quest (1999)',
          'laxy of Terror (1981)',
          'Galaxy Turnpike (2015)',
          'Zllipoli (1981 & 2005)']
gmovies = []
for title in movies:
    if title.startswith('G'):
        gmovies.append(title)

print(gmovies)
g_let_movies = [title for title in movies if title.startswith('G')]
print(g_let_movies)

movies_year = [('bbeh', 1997),
               ('Gabriel', 2007),
               ('abriel Over the White House', 1933),
               ('Zllipoli', 2005)]

year_mo = [title for (title, year) in movies_year if year > 2000]
print(year_mo)
