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
warnings.simplefilter(action='ignore', category=FutureWarning)

file_path = "C:/Users/jstco/Downloads/"

oln = pd.read_excel(file_path + 'Online Retail.xlsx', skipfooter = 541000)
print(oln.info())
# print(oln.head())

#########################
# infomation columns
# InvoiceNo: 주문번호
# StockCode: 상품코드
# Description: 상품 설명
# Quantity: 수량
# InvoceDate: 주문날짜
# UnitPrice: 개별 가격
# CustomerID: 고객번호
# Country: 국가
#########################

## 범주형
# invoiceno, stockcode, description, customerid, country

## 연속형
# quantity, invoicedate(시간변수), unitprice

# print(oln.describe())

## 데이터 살펴보기
# print('Total Data count : ', oln.shape[0] * oln.shape[1])
# nan = oln.isnull().sum().sum()
# nan_rate = nan / oln.shape[0] * 100
# print('NaN count : ', nan)
# print('NaN rate : ', nan_rate)

## 컬렴명 소문자로 변경
# oln.columns = oln.columns.str.lower()
# print(oln.isnull().sum(axis = 0))

## 결측치 있는 컬럼 확인하기
# nan_col = oln[oln.isnull().any(axis = 1)].head()

## ID가 없는 데이터 제거
# oln1 = oln.dropna()
# print(oln1.info())

# oln1['customerid'] = oln1['customerid'].astype('int64')
