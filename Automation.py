### 1. Create Random Data

# import time
# import random
# import os
#
# print('Process Started')
#
# start_time = time.time()
# num_samples = 100
# alphabet_samples = 'ancdefghijklmnopqrstuvwxyz1234567890'
#
#
# def random_string(length):
# 	return ''.join(random.choice(alphabet_samples) for i in range(length))
#
#
# nm_first = '김이박최정강조윤장임'
# nm_mid = '카를로스호나우두히바우두'
# nm_last = '호나우딩요카카카푸주닝요'
#
#
# def random_name(length):
# 	result = ''
# 	result += random.choice(nm_first)
# 	result += random.choice(nm_mid)
# 	result += random.choice(nm_last)
# 	return result
#
#
# file_path = 'C:/Users/jstco/Downloads/python 업무자동화'
# os.chdir(file_path)
# os.mkdir('random_data')

# for i in range(num_samples):
# 	name = random_name(3)
# 	file_name = str(i) + '_' + name + '.txt'
# 	file_path = 'random_data/' + file_name
# 	f = open(file_path, 'w')
# 	f.write('name : ' + name + '\n')
# 	f.write('age : ' + str(time.time())[-2:] + '\n')
# 	f.write('e-mail : ' + random_string(8) + '@or.kr' + '\n')
# 	f.write('division : ' + random_string(3) + '\n')
# 	f.write('telephone : 010-' + str(time.time())[-4:] + '-' + str(time.time())[-6:-2] + '\n')
# 	f.write('gender : ' + random.choice(['male', 'female']))
# 	f.close()

# print('Process Completed')

# end_time = time.time()
# print('Time Taken :' + str(end_time - start_time) + ' seconds')

### 2. merge data

# import time
# import os
#
# PATH = 'C:/Users/jstco/Downloads/python 업무자동화/random_data/'
# outfile_name = 'random_data_merge_1.csv'
# out_file = open(os.path.join(PATH, outfile_name), 'w')
# input_files = os.listdir(PATH)
# print(input_files)

# print('Process Started')
#
# start_time = time.time()
#
# for file_name in input_files:
# 	if '.txt' not in file_name:
# 		continue
#
# 	file = open(os.path.join(PATH, file_name), 'r')
# 	content = file.read()
# 	out_file.write(content + '\n')
# 	file.close()
# out_file.close()
#
# print('Process Completed')
# end_time = time.time()
#
# print('Time Taken :' + str(end_time - start_time) +'seconds')

### 3. merge text files
# import time
# import os
#
# PATH = 'C:/Users/jstco/Downloads/python 업무자동화/random_data'
# print('process started')
#
# start_time = time.time()
#
# outfile_name = 'random_data_merge_2.txt'
# out_file = open(os.path.join(PATH, outfile_name), 'w')
# input_files = os.listdir(PATH)
#
# for file_name in input_files:
# 	if '.txt' not in file_name:
# 		continue
#
# 	file = open(os.path.join(PATH, file_name), 'r')
# 	content = file.read()
# 	out_file.write(content + '\n')
#
# 	file.close()
#
# out_file.close()
#
# print('process completed')
# end_time = time.time()
#
# print('time taken :' + str(end_time - start_time) +'seconds')

### 4. merge into csv
import time
import os

print('process started')

start_time = time.time()
PATH = 'C:/Users/jstco/Downloads/python 업무자동화/random_data/'
outfile_name = 'random_data_merge_3.csv'

outfile = open(os.path.join(PATH, outfile_name), 'w')
input_files = os.listdir(PATH)

headers = []
outfile_has_header = False

for file_name in input_files:
	if '.txt' not in file_name:
		continue

	file = open(os.path.join(PATH, file_name))
	contents = []

	for line in file:
		if ':' in line:
			splits = line.split(':')
			contents.append(splits[-1].strip())

			if len(contents) > len(headers):
				headers.append(splits[0].strip())

	if not outfile_has_header:
		header = ', '.join(headers)
		outfile.write(header)
		outfile_has_header = True

	new_line = ', '.join(contents)
	outfile.write('\n' + new_line)

	file.close()

outfile.close()

print('process completed')

end_time = time.time()
print('time taken :' + str(end_time - start_time) + 'seconds')
