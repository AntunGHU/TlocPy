# Kako za stotine studenata automatski naci visu ocjenu i predstaviti to u obliku dict-a
# fg = {'dan':98, 'ang':91, 'kate':78}
midterms = [80,91,78]
finals = [98,89,53]
students = ['dan', 'ang', 'kate']

#* Sa zip i DictComprehension
# 1.LC i zip
final_grades = [pair for pair in zip(midterms, finals)]
print(final_grades)
# 2.dodavanje max-func
f_g = [max(pair) for pair in zip(midterms, finals)]
print(f_g)
# 3.LC u DictCompr, dodavanje studenata u zip
fg = {t[0]:max(t[1],t[2]) for t in zip(students, midterms, finals)}
print(fg)

#* Sa map, lambda i zip
# 1.Nalazenje vise ocjene
scores = list(map(lambda pair: max(pair), zip(midterms,finals)))
print(scores)
# 2.dodavanje studenata jos jednim zipovanjem
grades = list(zip(students, map(lambda pair: max(pair), zip(midterms,finals))))
print(grades)
# 3.konverzija zip-objekta u dict
grades = dict(zip(students, map(lambda pair: max(pair), zip(midterms,finals))))
print(grades)

#* Dobijanje procjecne ocjene: umjesto max(pair) staviti ((pair[0]+pair[1])/2)
avarage_grades = dict(zip(students, map(lambda pair: ((pair[0]+pair[1])/2), zip(midterms,finals))))
print(avarage_grades)