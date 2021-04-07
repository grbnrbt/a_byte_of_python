print('Простое присваивание')
shop_list = ['яблоки', 'манго', 'морковь', 'бананы']
my_list = shop_list  # my_list - лишь еще одно имя, указывающее на тот же
# объект

del shop_list[0]  # Ясделал первую покупку, поэтому удаляю ее из списка

print('shop_list:', shop_list)
print('my_list:', my_list)

print('Копирование при помощи полной вырезки')
my_list = shop_list[:]  # создаем копию путем полной вырезки
del my_list[0]  # удаляем первый элемент

print('shop_list:', shop_list)
print('my_list', my_list)
