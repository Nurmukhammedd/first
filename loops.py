# from ast import Expression
# from tkinter import Variable


# while Expression:
    # <body>



# i = 1
# while i <= 10:
#     print(f'Цикл выполнился {i}, раз')
#     i += 1 # i = i = 1
# print("Цикл закончился")

# i = 0
# name1 = ''
# name2 = ''
# while name1.lower() != 'john' and name2 != 'raychel':
#     name1 = input('Vvedite imya1:')
#     name2 = input('wwedite imya2:')
#     i += 1
#     if i > 5 :
#         print('Цикл остановлен')
#         break 
# else:
#     print('вы ввули правильное имя')


# admin = ['John', 'ilovepython']
# i = 3
# password = None

# while admin[1] != password:
#     password = input('John vvedite parol:')
#     i -= 1
#     if i == 0:
#         print('vy zablokirovany')
#         break
# else:
#     print('john vy voshli v sistemy')





# for <Variable> in <iter object>:
    # <body>
# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# for item in pizza:
    # print(f'Eating {item} of pizza')





# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []
# for item in pizza:
#     new_item = item.split('_')
    
#     spisok.append(new_item[0].capitalize())
# print(spisok)



# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []
# i = 0
# while i < len(pizza):
#     new_item = pizza[i].split('_')[0].capitalize()
#     spisok.append(new_item)
#     i += 1
# print(spisok)






# str_=[1,2,3,4,5]
# i=str_.__iter__()
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())
# print(i.__next__())



# nums = [2,7,11,13] 
# target = 9
# for x in nums:
#     n = target - x 
#     if n in nums:
#         print(x,n)


# nums = [2,7,11,13]
# target = 9
# for i in range(0, len(nums)):
#     num = target - nums[i]
#     if num in nums: 
#         if num == nums:
#             continue
#         k = nums.index(num)
#         print(f'otvet:{i}, {k}')
#         break




pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
spisok = []
for x in pizza:
    if x.startswith('fourth'):
        continue
    else:
        spisok.append(x)
print(spisok)