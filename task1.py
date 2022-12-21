# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint as rnd

k = int(input('Введите степень многочлена: '))
polynomial = []
for i in range(k, -1, -1):
    rnd_num = rnd(0, 100)
    if rnd_num == 0:
        continue
    if i == 1:
        polynomial.append(f' {rnd_num}*x ')
    elif i == 0:
        polynomial.append(f' {rnd_num} ')
    else:
        if rnd_num == 1:
            polynomial.append(f' x^{i} ')
        else:
            polynomial.append(f' {rnd_num}*x^{i} ')
string_to_file = ('+'.join(polynomial) + '= 0').strip()
text_file = open('file.txt', 'w')
text_file.writelines(string_to_file)
text_file.close()
