#Задание состоит из двух частей. 
#1 часть – написать программу в соответствии со своим вариантом задания.
#2 часть – усложнить написанную программу, введя по своему усмотрению 
# в условие минимум одно ограничение на характеристики объектов 
# и целевую функцию для оптимизации решения.

# Вариант 30. В филармонии К музыкальных инструментов (музыкантов). Сформировать все возможные варианты квартетов.

# 2 часть
# Ограничение: в квартете не могут находиться одновременно четные и нечетные, по порядковому номеру, музыкальные инструменты

import itertools

while True:
    num_instruments = int(input("Введите количество музыкальных инструментов: "))
    if num_instruments > 0:
        break

instruments_nechet = []
quartets_nechet = list()

def instrumentsnechet(n):
    for i in range(1, n + 1):
        if i % 2 != 0:
            instruments_nechet.append("Инструмент {}".format(i))
        quartets_nechet = list(itertools.combinations(instruments_nechet, 4))
    return quartets_nechet

count_nechet = 0


instruments_chet = []
quartets_chet = list()

def instrumentschet(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            instruments_chet.append("Инструмент {}".format(i))
        quartets_chet = list(itertools.combinations(instruments_chet, 4))
    return quartets_chet

count_chet = 0

print("Каждое число подразумевает название или номер отдельного инструмента")

print("Все возможные квартеты, состоящие из нечетных, по порядковому номеру, инструментов:")
for quartet in instrumentsnechet(num_instruments):
    count_nechet += 1
    print(quartet)
print("Количество всех возможных вариантов квартета, состоящих из нечетных, по порядковому номеру, инструментов: ",count_nechet)


print("Все возможные квартеты, состоящие из четных, по порядковому номеру, инструментов:")
for quartet in instrumentschet(num_instruments):
    count_chet += 1
    print(quartet)
print("Количество всех возможных вариантов квартета, состоящих из четных, по порядковому номеру, инструментов: ",count_chet)

count_general = count_chet + count_nechet

print("Общее количество всех возможных вариантов квартета: ",count_general)