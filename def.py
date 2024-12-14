def get_matrix(n, m, value): #создали функцию с тремя параметрами m,n,value
    matrix = [] # создали пустой список
    for i in range(n): # цикл для строк матрицы в n повторов
        matrix.append([]) #добавляем пустой список в список matrix
        for j in range(m): #создали внутренний цикл для столбцов матрицы в m повторов
            matrix[i].append(value) #пополняем значениями value ранее добавленный пустой список
    return matrix #возвращаем значение переменной matrix
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)