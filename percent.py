"""Вам дан словарь per_cent с распределением процентных 
ставок по вкладам в различных банках таким образом, 
что ключ — название банка, значение — процент. 
Напишите программу, в результате которой будет сформирован
список deposit значений — накопленные средства за год 
вклада в каждом из банков. На вход программы с клавиатуры 
вводится сумма money, которую человек планирует положить под проценты."""

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму вклада '))
deposit = []
for i in per_cent:
   result = int(per_cent[i] * money / 100)  
   deposit.append(result)
# max_deposit = max(deposit)
print('deposit = ' + str(deposit))
# print("Максимальная сумма, которую вы можете заработать — " + str(max_deposit))
print("Максимальная сумма, которую вы можете заработать — " + str(max(deposit)))
