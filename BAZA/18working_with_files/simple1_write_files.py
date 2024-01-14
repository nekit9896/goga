file = open('text.txt', 'w')  # если такого файла нет - он будет создан и открыт, если файл есть - он будет открыт
file.write('Hi')
file.write('!')
file.write('\nI am')  # запись с новой строки \n
"""
Существует несколько способов открытия файлов:
'r' - открытие для чтения (является значение по умолчанию)
'w' - открытие файлы для записи. 
Если файл существует, то его содержимое удаляется, а файл готов к записи нового содержимого.
Если файла не существует, то создается новый готовый к записи
'x' - открытие файла для записи только если файла не существует
'a' - открытие файла для дозаписи, информация добавляется в конец файла
'b' - открытие в двоичном режиме
't' - открытие в текстовом режиме (является значением по умолчанию)
'+' - открытие на чтение и запись
"""
file.close()  # закрыть файл чтоб не было утечки памяти
file1 = open('text1.txt', 'a')
file1.write("SSSS")
file1.write("ava")
file1.close()


def file_writer():
    file2 = open('text2.txt', 'a')
    text = input(str("Введите текст: "))
    file2.write(text + '\n')
    file2.close()


file_writer()








