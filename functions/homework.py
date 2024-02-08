#Программист написал функцию, но она не работает. Исправьте все ошибки!
#В функцию передается возраст одного из 3 людей с помощью позиционного аргумента и сегодняшний год.
#Выводится должна лишь одна дата, остальные можете заменить на 0. # 0 2007 0
#Код можно изменять как угодно.

def birth_year(age_people1=17, age_people2=0, age_people3, year_now):
    birth1 = year_now - age_people1
    birth2 = year_now - age_people2
    birth3 = year_now - age_people3

birth = birth_year(age_people2=16, 2024)
print(birth)
    
