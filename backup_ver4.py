import os
import time
import zipfile

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['./_code', './_docs']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = './_backup'  # бекапы будем записывать сюда
if not os.path.exists(target_dir):  # если каталога нет
    os.mkdir(target_dir)  # создаем каталог

# 3. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + '/' + time.strftime('%Y%m%d')
if not os.path.exists(today):  # проверяем наличие каталога
    os.mkdir(today)  # создаем каталог
    print('Каталог успешно создан', today)

# Текущее время служит именем zip-архива
now = time.strftime('%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:  # проверяем, введен ли комментарий
    target = today + '/' + now + '.zip'
else:
    target = today + '/' + now + '_' + comment.replace(' ', '_') + '.zip'

# 5. Обращаемся к модулю zipfile для архивации
zip_file = zipfile.ZipFile(target, 'w')

# Записываем папки в архив
for s in source:
    for root, dirs, files in os.walk(s):
        for file in files:
            zip_file.write(os.path.join(root, file))

# Закрываем архив
zip_file.close()
