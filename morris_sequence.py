class Morris:
    '''Класс, на основе кода которого будет выполнена последовательность Морриса, где n - количество итераций.'''

    def calculate(self, n):
        self.n = n
        '''Определяем число итераций'''


        # Первое число последовательности
        number = 1
        # Количество повторений одного и того же символа
        count = 1
        # Список для последовательности
        list = []

        for i in range(n):
            if i != 0:
                # Перевод предыдущего результата последовательности в строку для дальнейшего перебора
                tmp = str(number)

                # Переменная для результата
                tmp_result = ''

                # Перебор каждого элемента предыдущего результата
                for j in range(len(tmp)):
                    if j == len(tmp) - 1 or tmp[j] != tmp[j + 1]:
                        tmp_result += str(count) + tmp[j]
                        count = 1
                    else:
                        count += 1

                number = int(tmp_result)

            # Занесение результата в массив
            list.append(number)

        # Вывод элементов массива
        for r in list:
            print(r)

# Далее создаем объект класса и запускаем метод:
first = Morris()
first.calculate(5)