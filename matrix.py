import numpy as np
import csv

M = int(input("Введите 1ю сторону матрицы: "))
N = int(input("Введите 2ю сторону матрицы: "))

random_matrix = np.random.rand(M, N)

filename = input('filename: ')
filename = str(filename)

if filename == "" or " ":
    print(random_matrix)
else:
    with open(filename+ '.csv', mode="w", encoding='utf-8') as w_file:
        file_writer = csv.writer(w_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(random_matrix)
