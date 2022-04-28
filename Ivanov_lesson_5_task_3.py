def my_gen(items1, items2):
    t = len(items1) - len(items2)
    if t > 0:
        for _ in range(k):
            items2.append(None)
    for tutor, klass in zip(items1, items2):
        yield (tutor, klass)


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '9А'
]

my_gener = my_gen(tutors, klasses)
print(next(my_gener))
print(next(my_gener))
print(next(my_gener))
print(next(my_gener))
print(next(my_gener))
print(next(my_gener))
print(next(my_gener))
print(next(my_gener))
print(next(my_gener))
print(next(my_gener))
print(next(my_gener))
