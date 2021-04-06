# Это мой список покупок
shop_list = ['яблоки', 'манго', 'морковь', 'бананы']

print('Я должен сделать', len(shop_list), 'покупки.')

print('Покупки:', end=' ')
for item in shop_list:
    print(item, end=' ')

print('\nТакже нужно купить риса.')
shop_list.append('рис')
print('Теперь список покупок таков:', shop_list)

print('Отсортирую-ка я свой список')
shop_list.sort()
print('Отсортированный список покупок выглядит так:', shop_list)

print('Первое что мне нужно купить, это', shop_list[0])
old_item = shop_list[0]
del shop_list[0]
print('Я купил', old_item)
print('Теперь мой список покупок:', shop_list)
