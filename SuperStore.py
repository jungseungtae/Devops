import math
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8')
sns.set(font_scale = 1)
plt.rc('font', family = 'Maruburi')
plt.rcParams['font.family'] = 'Maruburi'

import warnings

warnings.simplefilter(action = 'ignore', category = FutureWarning)

file_path = "C:/Users/jstco/Downloads/"
sp = pd.read_csv(file_path + 'Superstore Data.csv')

## file browsing
# print(sp.info())
# print(sp.head())
# print(sp.describe())
# print(sp.describe(include = np.object))
# print(sp.describe(include = object))

# total_data = sp.shape[0] * sp.shape[1]
# nan_data = sp.isnull().sum().sum()
# nan_rate = (nan_data * 100) / total_data
# data_period_min = min(sp['Order Date'])
# data_period_max = max(sp['Order Date'])
# total_selling_products = sp['Product ID'].nunique()
#
# print(f'Total data: {total_data:,}, nan data: {nan_data}, nan rate: {nan_rate} \n'
# f'data period is {data_period_min} ~ {data_period_max} \n'
# f'total selling products: {total_selling_products:,}')

## double check
# print(sp.duplicated().sum())=
# print(sp.columns)

## columns preprocessing
sp.columns = sp.columns.str.lower()
sp.columns = sp.columns.str.replace(' ', '_')
# print(sp.columns)
# sp1 = sp.drop(['post_code'], axis = 1)
sp1 = sp.drop(['postal_code'], axis = 1)
# print(sp1.info())

'''''''''''''''''''''
row_id	int64
order_id	object
order_date	object
ship_date	object
ship_mode	object
customer_id	object
customer_name	object
segment	object
country	object
city	object
state	object
region	object
product_id	object
category	object
sub-category	object
product_name	object
sales	float64
quantity	int64
discount	float64
profit	float64
sub-category	object
product_name	object
sales	float64
quantity	int64
discount	float64
profit	float64
'''''''''''''''''''''

# order top_10
# sp1 = sp1['product_name'].value_counts().sort_values(ascending = False)[:10]
# print(sp1)

# 카테고리별 판매금액과 할인율의 분포
# f, ax = plt.subplots(1, 2, figsize = (13, 7))
#
# sns.violinplot(x = sp['category'], y = sp1['sales'], ax = ax[0])
# sns.violinplot(x = sp['category'], y = sp1['discount'] * 100, ax = ax[1])
# plt.figure(figsize = (12, 10))
# sp['sub-category'].value_counts().plot.pie(autopct = '%1.1f%%')
#
# plt.show()

# 도시별 주문량 10.
# top_cities = sp['city'].value_counts().nlargest(10)
# print(top_cities)

# top_state = sp['state'].value_counts().nlargest(10)
# print(top_state)
# top_state = sp['state'].value_counts().nlargest(10)
# print(top_state)

f, ax = plt.subplots(1, 1, figsize = (18, 8))

# g = sns.countplot(top_state, ax = ax)
g = sns.countplot(sp1['city'].value_counts().nlargest(10), ax=ax)
g.set_xticklabels(g.get_xticklabels(), rotation = 90)
g.set_title('State', size = 15)
g.set_ylabel('Count', size = 15)

plt.show()