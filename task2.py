# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

first_file = open('firstFile.txt', 'r')
first_poly = first_file.read()
first_file.close()
second_file = open('scndFile.txt', 'r')
second_poly = second_file.read()
second_file.close()
first_poly = first_poly.split(' = ')
first_poly = first_poly[0].split(' + ')
second_poly = second_poly.split(' = ')
second_poly = second_poly[0].split(' + ')
first_poly_k = []
second_poly_k = []
for item in first_poly:
    first_poly_k.append(item.split('x'))
for item in second_poly:
    second_poly_k.append(item.split('x'))
print(first_poly_k)
print(second_poly_k)
for i in range(len(first_poly_k)):
    if len(first_poly_k[i]) == 1:
        first_poly_k[i][0] = int(first_poly_k[i][0])
    else:
        if first_poly_k[i][0] == '':
            first_poly_k[i][0] = 1
            first_poly_k[i][1] = int(first_poly_k[i][1].replace('^', ''))
        elif first_poly_k[i][1] == '':
            first_poly_k[i][0] = int(first_poly_k[i][0].replace('*', ''))
            first_poly_k[i][1] = 1
        else:
            first_poly_k[i][0] = int(first_poly_k[i][0].replace('*', ''))
            first_poly_k[i][1] = int(first_poly_k[i][1].replace('^', ''))
for i in range(len(second_poly_k)):
    if len(second_poly_k[i]) == 1:
        second_poly_k[i][0] = int(second_poly_k[i][0])
    else:
        if second_poly_k[i][0] == '':
            second_poly_k[i][0] = 1
            second_poly_k[i][1] = int(second_poly_k[i][1].replace('^', ''))
        elif second_poly_k[i][1] == '':
            second_poly_k[i][0] = int(second_poly_k[i][0].replace('*', ''))
            second_poly_k[i][1] = 1
        else:
            second_poly_k[i][0] = int(second_poly_k[i][0].replace('*', ''))
            second_poly_k[i][1] = int(second_poly_k[i][1].replace('^', ''))
sum_str = []
if len(first_poly_k) > len(second_poly_k):
    for i in range(len(first_poly_k) - 1):
        for j in range(len(second_poly_k) - 1):
            if first_poly_k[i][1] == second_poly_k[j][1]:
                first_poly_k[i][0] += second_poly_k[j][0]
        if first_poly_k[i][1] == 1:
            sum_str.append(f' {first_poly_k[i][0]}*x ')
        elif first_poly_k[i][0] == 1:
            sum_str.append(f' x^{first_poly_k[i][1]} ')
        else:
            sum_str.append(f' {first_poly_k[i][0]}*x^{first_poly_k[i][1]} ')
    sum_str.append(' ' + str(first_poly_k[len(first_poly_k)-1][-1] + second_poly_k[len(second_poly_k)-1][-1]) + ' ')

else:
    for i in range(len(second_poly_k) - 1):
        for j in range(len(first_poly_k) - 1):
            if second_poly_k[i][1] == first_poly_k[j][1]:
                second_poly_k[i][0] += first_poly_k[j][0]
        if second_poly_k[i][1] == 1:
            sum_str.append(f' {second_poly_k[i][0]}*x ')
        elif second_poly_k[i][0] == 1:
            sum_str.append(f' x^{second_poly_k[i][1]} ')
        else:
            sum_str.append(f' {second_poly_k[i][0]}*x^{second_poly_k[i][1]} ')
    sum_str.append(' ' + str(second_poly_k[len(second_poly_k)-1][-1] + first_poly_k[len(first_poly_k)-1][-1]) + ' ')
string_to_file = ('+'.join(sum_str) + '= 0').strip()
text_file = open('file_task2.txt', 'w')
text_file.writelines(string_to_file)
text_file.close()
