# stroka1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# vowels = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
# phrases = stroka1.split()
# if len(phrases) < 2:
#     print('Количество фраз должно быть больше одной!')
# else:
#     countVowels = []

# for i in phrases:
#     countVowels.append(len([x for x in i if x.lower() in vowels]))

# if countVowels.count(countVowels[0]) == len(countVowels):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# cities = 'Шымкент Алматы Астана Уфа'.split()
# res_cities = [ 1 for _ in cities if len(_) > 5]
# print(*res_cities)
N = 5
list = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
for i in list:
    print(*i)



list2 = [[1 if i == j else 0 for j in range(N)] for i in range(N)]


s = '-8 15 20 126 -40'

print(*filter(lambda x: 9 < abs(int(x)) < 100, s.split()))























list12 = [[1 if i == j else 0 for j in range(N)] for i in range(N)]


s = '10 18 -20 1 99 100 160'
print( *filter(lambda x: len(str(abs(int(x)))) == 2,  s.split()))






list1 = [[1 if i == j else 0 for j in range(N)] for i in range(N)]
print(*list12)



