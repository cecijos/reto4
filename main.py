# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import Serie


bm0 = Serie.Serie ("Los Simpsons", 25, "Humor", "Matt Groening")
bm1= Serie.Serie ("Padre de familia", 10 ,"Humor bizarro", "Seth MacFarlane")
bm2= Serie.Serie("Breaking Bad", 5, "Thriller", "Vince Gilligan")
bm3= Serie.Serie("Benito y Manolo", 35, "Humor castizo", "Desconocido")
bm4= Serie.Serie("Curro Jimenez", 40, "Bandoleros", "Mario Camus")
juego0= Serie.Videojuego('tetris','diversion',22,'cdprojectk')
juego1=Serie.Videojuego('mario','aventura',145,'konami')
juego2=Serie.Videojuego('cars','carreras',99,'konami')
juego3=Serie.Videojuego('sonic','aventura',85,'sega')
juego4=Serie.Videojuego('fifa','deportes',75,'easports')
listaserie=[bm0,bm1,bm2,bm3,bm4]
listajuego=[juego0,juego1,juego2,juego3,juego4]



listaserie[1].entregar()
e=listaserie[1].estado1()
listaserie[0].devolver()
g=listaserie[0].estado1()
listaserie[2].entregar()
z=listaserie[2].estado1()


entre_serie=[e,g,z]


def count(entre_serie):
  return sum(bool(x) for x in entre_serie)
print ("Hay " + str(count(entre_serie)) + " series entregadas")
listaserie[0].devolver()
listaserie[1].devolver()
listaserie[2].devolver()





listajuego[3].entregar()
ee=listajuego[3].estado1()
listajuego[4].devolver()
ff=listajuego[4].estado1()
entre_juego=[ee,ff]

def count(entre_juego):
  return sum(bool(x) for x in entre_juego)
print ("Hay " + str(count(entre_juego)) + " juegos entregados")
listajuego[3].devolver()
listajuego[4].devolver()


p=listaserie[0].get_numerotemporadas()
q=listaserie[1].get_numerotemporadas()
r=listaserie[2].get_numerotemporadas()
s=listaserie[3].get_numerotemporadas()
t=listaserie[4].get_numerotemporadas()
maxtemporadas=[p,q,r,s,t]


print('La serie con mas temporadas tiene '+ str(max([int(num) for num in maxtemporadas])))
max_position1=maxtemporadas.index(max(maxtemporadas))
#print(max_position1)
print(str(listaserie[max_position1]))

pp=listajuego[0].get_horasestimadas()
qq=listajuego[1].get_horasestimadas()
rr=listajuego[2].get_horasestimadas()
ss=listajuego[3].get_horasestimadas()
tt=listajuego[4].get_horasestimadas()
maxhorasestimadas=[pp,qq,rr,ss,tt]
print('El juego con mas horas de juego tiene '+ str(max([int(num) for num in maxhorasestimadas])))
max_position=maxhorasestimadas.index(max(maxhorasestimadas))
#print(max_position)
print(str(listajuego[max_position]))

