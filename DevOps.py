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
# kv_list = {'k1': 'v1', 'k2': 'v2'}
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

# def no_return():
# 	''
# 	pass
#
# result = no_return()
# print(result)

# def return_one():
# 	return 1
#
# result = return_one()
# print(result)

## object function
# def double(input):
# 	return input * 2
#
# # print(double)
#
# def triple(input):
# 	return input * 3
#
# functions = [double, triple]
# # print(functions)
#
# for function in functions:
# 	print(function(10))

## anonymous function
# items = [[0, 'a', 2], [5, 'b', 3], [10, 'c', 4]]
# print(sorted(items))

# def second(item):
# 	return item[1]

# print(sorted(items, key=second))
# sorted_items = sorted(items, key=lambda item: item[1])
# sorted_items2 = sorted(items, key=lambda item: item[2])

# print(sorted_items)
# print(sorted_items2)

# cc_list = '''Ezra Koening<ekoenig@vpwk.com>,
# Rostam Batmaglij <rostam@vpwk.com>,
# Chris Tomson <chris@vpwk.com>,
# Bobbi Baio <bobbi@vpwk.com>
# '''

# print('Rostam' in cc_list)
import re
# print(re.search('Rostam', cc_list))

# if re.search('Rostam', cc_list):
# 	print('Rostam found')

## Character set
# print(re.search(r'[RB]obb[i,y]', cc_list))
# print(re.search(r'chr[a-z][a-z]', cc_list))
# print(re.search(r'[A-Za-z]+', cc_list))
# print(re.search(r'[A-Za-z]{6}', cc_list))
# print(re.search(r'[A-Za-z]+@[a-z]+\.[a-z]+', cc_list))

## Character class
# print(re.search(r'\w+', cc_list)) # \w+ = [a-zA-Z0-9_]
# print(re.search(r'\w+\@\w+\.\w+', cc_list))

## group
# matched = re.search(r'(\w+)\@(\w+)\.(\w+)', cc_list)
# print(matched)
# print(matched.group(0))   # 0 = all matches
# print(matched.group(1))   # n = each matches

## named groups
# matched = re.search(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
# print(matched.group('name'))
# print(f'''name : {matched.group('name')}
# Secondary Level Domain : {matched.group('SLD')}
# Top Level Domain : {matched.group('TLD')}
# ''')

## find all
# matched = re.findall(r'\w+\@\w+\.\w+', cc_list)
# print(matched)
# matched = re.findall(r'(\w+)\@(\w+)\.(\w+)', cc_list)
# # print(matched)
# names = [x[0] for x in matched]
# print(names)

## find repeated
# matched = re.finditer(r'\w+\@\w+\.\w+', cc_list)
# # print(list(matched))
# print(matched)
# print(next(matched))
# print(next(matched))
# print(next(matched))

# matched = re.finditer(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)', cc_list)
# print(list(matched))
# for m in matched:
# 	print(m.groupdict())

## substition
# sub = re.sub('\d', '#', 'The passcode you entered is 09876')
# print(sub)
# users = re.sub('(?P<name>\w)+\@(?P<SLD>\w)\.(?P<TLD>\w)', '\g<TLD>.\g<SLD>.\g<name>', cc_list)
# print(users)

## compile
# regex = re.compile(r'\w+\@\w+\.\w+')
# print(regex.search(cc_list))

## lazy evaluation
# def count():
# 	n = 0
# 	while True:
# 		n += 1
# 		yield n
#
# counter = count()
# print(counter)
# print(next(counter))
# print(next(counter))
# print(next(counter))

# def fib():
# 	first = 0
# 	last = 1
# 	while True:
# 		first, last = last, first + last
# 		yield first
#
# f = fib()
# # print(next(f))
# # print(next(f))
# # print(next(f))
#
# for x in f:
# 	print(x)
# 	if x > 12:
# 		break

## generate connotation
# list_o_nums = [x for x in range(10)]
# gen_o_nums = (x for x in range(10))
# print(list_o_nums)
# print(gen_o_nums)

## return size
# import sys
# list_b = sys.getsizeof(list_o_nums)
# gen_b = sys.getsizeof(gen_o_nums)
# print(list_b)
# print(gen_b)

## os
import os
# print(os.getcwd())
# print(os.listdir())
## rename, chmod, mkdir, makedirs, remove, rmdir, removedirs

# cur_dir = os.getcwd()
# print(cur_dir)
# print(os.path.split(cur_dir))
# print(os.path.dirname(cur_dir))
# print(os.path.basename(cur_dir))

# def find_rc(rc_name = '.examplerc'):
# 	var_name = 'EXAMPLERC_DIR'
# 	if var_name in os.environ:
# 		var_path = os.path.join(f'${var_name}', rc_name)
# 		config_path = os.path.expandvars(var_path)
# 		print(f'Checking {config_path}')
# 		if os.path.exists(config_path):
# 			return config_path
#
# 	config_path = os.path.join(os.getcwd(), rc_name)
# 	print(f'Checking {config_path}')
# 	if os.path.exists(config_path):
# 		return config_path
#
# 	home_dir = os.path.expanduser('~')
# 	config_path = os.path.join(home_dir, rc_name)
# 	print(f'Checking {config_path}')
# 	if os.path.exists(config_path):
# 		return config_path
#
# 	file_path = os.path.abspath(__file__)
# 	parent_path = os.path.dirname(file_path)
# 	config_path = os.path.join(parent_path, rc_name)
# 	print(f'Checking {config_path}')
# 	if os.path.exists(config_path):
# 		return config_path
#
# 	print(f'File {rc_name} has not been found')

import fire

# def walk_path(parent_path):
# 	print(f'Walking {parent_path}')
# 	childs = os.listdir(parent_path)
#
# 	for child in childs:
# 		child_path = os.path.join(parent_path, child)
# 		if os.path.isfile(child_path):
# 			last_access = os.getatime(child_path)
# 			size = os.path.getsize(child_path)
# 			print(f'{child_path} - {last_access} - {size}')
# 		elif os.path.isdir(child_path):
# 			walk_path(child_path)
#
# if __name__ == '__main__':
# 	fire.Fire()

# def walk_path(parent_path):
# 	for parent_path, directories, files, in os.walk(parent_path):
# 		print(f'Walking {parent_path}')
# 		for file_name in files:
# 			file_path = os.path.join(parent_path, file_name)
# 			last_access = os.getatime(file_path)
# 			size = os.path.getsize(file_path)
# 			print(f'{file_path} - {last_access} - {size}')
#
# if __name__ == '__main__':
# 	fire.Fire()

