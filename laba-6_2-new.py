#Задание состоит из двух частей. 
#1 часть – написать программу в соответствии со своим вариантом задания.
#2 часть – усложнить написанную программу, введя по своему усмотрению 
# в условие минимум одно ограничение на характеристики объектов 
# и целевую функцию для оптимизации решения.

# Вариант 30. В филармонии К музыкальных инструментов (музыкантов). Сформировать все возможные варианты квартетов.

# 2 часть
# Ограничение: в филармонии есть подразделение на группы инструментов, которые перечисленны ниже:
#струнные: скрипка, виолончель, альт, контрабас, арфа, гитара, комуз, хомус, кыяк, кобыз, домбыра, гусли, балалайка, домра
#деревянные духовые: флейта, гобой, кларнет, фагот, саксофон, блокфлейта, шалмей, шалюмо, балабан, дудук, жалейка, свирель, зурна, альбока
#медные духовые: валторна, труба, корнет, флюгельгорн, тромбон, туба, сакбут, серпент
#ударные: барабаны, тарелки, бубен, кастаньеты, треугольник, ксилофон, литавры, колокольчики, вибрафон

# Целевая функция: ищет квартет с наибольшим рейтингом инструментов (музыкантов)


instruments_1 = ["скрипка", "виолончель", "альт", "контрабас", "арфа", "гитара", "комуз", "хомус", "кыяк", "кобыз", "домбыра", "гусли", "балалайка", "домра"]
rate_levels_1 = {"скрипка": 1000, "виолончель": 700, "альт": 1000, "контрабас": 500, "арфа": 1400, "гитара": 900, "комуз": 400, "хомус": 100, "кыяк": 100, "кобыз": 150, "домбыра": 120, "гусли": 700, "балалайка": 800, "домра": 1000}

instruments_2 = ["флейта","гобой", "кларнет", "фагот", "саксофон", "блокфлейта", "шалмей", "шалюмо", "балабан", "дудук", "жалейка", "свирель", "зурна", "альбока"]
rate_levels_2 = {"флейта": 200, "гобой": 300, "кларнет": 900, "фагот": 430, "саксофон": 600, "блокфлейта": 340, "шалмей": 200, "шалюмо": 100, "балабан": 800, "дудук": 500, "жалейка": 1800, "свирель": 490, "зурна": 670, "альбока": 890} 

instruments_3 = ["валторна", "труба", "корнет", "флюгельгорн", "тромбон", "туба", "сакбут", "серпент"]
rate_levels_3 = {"валторна": 900, "труба": 800, "корнет": 2300, "флюгельгорн": 1300, "тромбон": 1400, "туба": 380, "сакбут": 400, "серпент": 230}

instruments_4 = ["барабаны", "тарелки", "бубен", "кастаньеты", "треугольник", "ксилофон", "литавры", "колокольчики", "вибрафон"]
rate_levels_4 = {"барабаны": 400, "тарелки": 650, "бубен": 1500, "кастаньеты": 4300, "треугольник": 520, "ксилофон": 680, "литавры": 900, "колокольчики": 1000, "вибрафон": 1430}

print('Выберете группу музыкальных инструментов')
while True:
    choice = input('Введите 1, если хотите выбрать струнные, 2 - деревянные духовые, 3 - медные духовые, 4 - ударные: ')
    if choice == '1' or choice == '2' or choice == '3' or choice == '4':
        break

if choice == '1':
    n = int(input('\nВведите количество музыкальных инструментов.' 
                '\nУчтите, что в распоряжении филармонии 14 струнных инструментов.\n'))
    while n < 4 or n > 14: 
        n = int(input('\nВведите натуральное число больше 3, но не больше 14:\n'))
    best_quartets = []
    max_rating = 0
    def top_rated_quartet(n, max_rating):
        for i in range(n):  #перебираем все возможные варианты
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for b in range(k + 1, n):
                        quartet = [instruments_1[i], instruments_1[j], instruments_1[k], instruments_1[b]]
                        rate_sum = sum([rate_levels_1[instrument] for instrument in quartet])
                        if rate_sum > max_rating: #находим максимальный рейтинг квартета
                            max_rating_combination = quartet
                            max_rating = rate_sum                              
                        best_quartets.append((quartet, rate_sum))
        
        print(f'Всего может быть составлено {len(best_quartets)} вариантов квартета из {n} инструментов.\n\n'
          f'Список комбинаций квартета из инструментов ({", ".join(instruments_1[:n])}) c общим рейтингом:\n')
        for count, quartet in enumerate(best_quartets, start=1):
            print(f'{count}. {" - ".join((str(x) for x in quartet))}')

        print('\nВариант квартета с наивысшим рейтингом:')

        return max_rating_combination, max_rating

    print(top_rated_quartet(n, max_rating))

if choice == '2':
    n = int(input('\nВведите количество музыкальных инструментов.' 
                '\nУчтите, что в распоряжении филармонии 14 деревянно духовых инструментов.\n'))
    while n < 4 or n > 14:  
        n = int(input('\nВведите натуральное число больше 3, но не больше 14:\n'))
    best_quartets = []
    max_rating = 0
    def top_rated_quartet(n, max_rating):
        for i in range(n):  #перебираем все возможные варианты
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for b in range(k + 1, n):
                        quartet = [instruments_2[i], instruments_2[j], instruments_2[k], instruments_2[b]]
                        rate_sum = sum([rate_levels_2[instrument] for instrument in quartet])
                        if rate_sum > max_rating: #находим максимальный рейтинг квартета
                            max_rating_combination = quartet
                            max_rating = rate_sum                              
                        best_quartets.append((quartet, rate_sum))
        
        print(f'Всего может быть составлено {len(best_quartets)} вариантов квартета из {n} инструментов.\n\n'
          f'Список комбинаций квартета из инструментов ({", ".join(instruments_2[:n])}) c общим рейтингом:\n')
        for count, quartet in enumerate(best_quartets, start=1):
            print(f'{count}. {" - ".join((str(x) for x in quartet))}')

        print('\nВариант квартета с наивысшим рейтингом:')

        return max_rating_combination, max_rating

    print(top_rated_quartet(n, max_rating))


if choice == '3':
    n = int(input('\nВведите количество музыкальных инструментов.' 
                '\nУчтите, что в распоряжении филармонии 8 медно духовых инструментов.\n'))
    while n < 4 or n > 8:  
        n = int(input('\nВведите натуральное число больше 3, но не больше 8:\n'))
    best_quartets = []
    max_rating = 0
    def top_rated_quartet(n, max_rating):
        for i in range(n):  #перебираем все возможные варианты
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for b in range(k + 1, n):
                        quartet = [instruments_3[i], instruments_3[j], instruments_3[k], instruments_3[b]]
                        rate_sum = sum([rate_levels_3[instrument] for instrument in quartet])
                        if rate_sum > max_rating: #находим максимальный рейтинг квартета
                            max_rating_combination = quartet
                            max_rating = rate_sum                              
                        best_quartets.append((quartet, rate_sum))
        
        print(f'Всего может быть составлено {len(best_quartets)} вариантов квартета из {n} инструментов.\n\n'
          f'Список комбинаций квартета из инструментов ({", ".join(instruments_3[:n])}) c общим рейтингом:\n')
        for count, quartet in enumerate(best_quartets, start=1):
            print(f'{count}. {" - ".join((str(x) for x in quartet))}')

        print('\nВариант квартета с наивысшим рейтингом:')

        return max_rating_combination, max_rating

    print(top_rated_quartet(n, max_rating))


if choice == '4':
    n = int(input('\nВведите количество музыкальных инструментов.' 
                '\nУчтите, что в распоряжении филармонии 9 ударных инструментов.\n'))
    while n < 4 or n > 9: 
        n = int(input('\nВведите натуральное число больше 3, но не больше 9:\n'))
    best_quartets = []
    max_rating = 0
    def top_rated_quartet(n, max_rating):
        for i in range(n):  #перебираем все возможные варианты
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for b in range(k + 1, n):
                        quartet = [instruments_4[i], instruments_4[j], instruments_4[k], instruments_4[b]]
                        rate_sum = sum([rate_levels_4[instrument] for instrument in quartet])
                        if rate_sum > max_rating: #находим максимальный рейтинг квартета
                            max_rating_combination = quartet
                            max_rating = rate_sum                              
                        best_quartets.append((quartet, rate_sum))
        
        print(f'Всего может быть составлено {len(best_quartets)} вариантов квартета из {n} инструментов.\n\n'
          f'Список комбинаций квартета из инструментов ({", ".join(instruments_4[:n])}) c общим рейтингом:\n')
        for count, quartet in enumerate(best_quartets, start=1):
            print(f'{count}. {" - ".join((str(x) for x in quartet))}')

        print('\nВариант квартета с наивысшим рейтингом:')

        return max_rating_combination, max_rating

    print(top_rated_quartet(n, max_rating))
