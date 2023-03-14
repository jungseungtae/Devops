"""""""""""""""""""""""""""
Chapter 1. Python Basics
"""""""""""""""""""""""""""

## except
# thinkers = ['Plato', 'PlayDo', 'Gumby']
# while True:
# 	try:
# 		thinker = thinkers.pop()
# 		print(thinker)
# 	except IndexError as e:
# 		print('We tried to pop too many thinkers')
# 		print(e)
# 		break

## append, insert, pop
# pies = ['cherry', 'apple', 'orange']
# pies.append('banana')
# print(pies)

# pies.insert(1, 'pear')
# print(pies)

# desserts = ['chocolate', 'strawberry', 'vanilla']
# desserts.extend(pies)
# print(desserts)

# pies.pop()
# print(pies)

# pies.pop(1)
# print(pies)

# pies.remove('cherry')

## list comprehensions
# squares = [x**2 for x in range(10)]
# print(squares)

# squares = [x**2 for x in range(10) if x % 2 == 0]
# print(squares)

# multi_line = '''
# This is a multi-line string
# '''
# print(multi_line)

## reduce the strip(strip, rstrip, lstrip)
# input = '   I want to reduce  " "   '
# print(input.strip())

## 적용안됨. ipython에서는 적용됨.
# output = 'barry'
# output.ljust(10)
# print(output)
# output.rjust(10, '*')
# print(output)

## split
# text = 'I want to split this text into words'
# words = text.split()
# print(words)
# url = 'https://www.google.co.kr/search?q=python'
# url.split('/')
# print(url.split('/'))

## join
# items = [1, 2, 3, 4, 5, 6]
# print(' and '.join(str(items)))

## change case
'''
capitalize, upper, title, swapcase, lower
'''

## Get String Content
'''
startswith, endswith, find, findall, index, count
'''

## string formatting
# sf = '{} comes before {}'.format('first', 'last')
# print(sf)

# sf2 = '{1} comes before {0}, but second comes bofore {2}'.format('first', 'second', 'third')
# print(sf2)

# lee = '''
# {country} is an island.
# {country} is off of the coast of
# {continent} in the {ocean}
# '''.format(country='USA', continent='Europe', ocean='Oceania')

# print(lee)

# values = {'first': 'John', 'last': 'Doe', 'age': 32}
# key = 'wont you come home {first} {last}. age is {age}'.format(**values)
# print(key)

# text = '|{0:>22}||{0:<22}|'
# text = '|{0:<>22}||{0:><22}|'
# print(text.format('0', '0'))

# count = 43
# print(f'|{count:5d}')

# from string import Template
# greeting = Template('$hello Mark Anthony')
# greeting.substitute(hello = 'Bonjour')
# print(greeting.substitute(hello = 'Bonjour'))

## dictionary
kv_list = {'k1': 'v1', 'k2': 'v2'}
# print(dict}(kv_list))
# if 'k4' in kv_list:
# 	print('k4 exists')
# else:
# 	print('k4 does not exist')
# dict(kv_list).get('k1', 'default value')
# print(dict(kv_list).get('k4', 'default value'))
# del(kv_list['k1'])
# print(kv_list)
# print(kv_list.keys())
# print(kv_list.values())
# letters = 'abcdefghijklmnopqrstuvwxyz'
# cap_map = {x:x.upper() for x in letters}
# print(cap_map)

## function
# def add(x, y):
# 	return x + y
# print(add(1, 2))

