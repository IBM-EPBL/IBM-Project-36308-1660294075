# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WwkwIhgJITUYejqOHSfFwvFE846ax7-O
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings 
warnings.filterwarnings('ignore')

d = pd.read_csv(r'abalone.csv')

d.head()

sns.boxplot(d['Diameter'])

plt.hist(d['Diameter'])

plt.plot(d['Diameter'].head(10))

plt.pie(d['Diameter'].head(),autopct='%.2f')

sns.distplot(d['Diameter'].head(200))

plt.scatter(d['Diameter'].head(500),d['Length'].head(500))

#bar plot

plt.bar(d['Sex'].head(10),d['Rings'].head(10))

#labelling of x,y and result

plt.title('Bar plot')
plt.xlabel('Diameter')
plt.ylabel('Rings')

sns.barplot(d['Sex'], d['Rings'])

sns.barplot(d['Diameter'].head(50),d['Rings'].head(50))

sns.jointplot('Diameter','Rings',hue='Sex',data=d.head())

sns.lineplot(d['Diameter'].head(),d['Rings'].head())

sns.boxplot(d['Sex'].head(10),d['Diameter'].head(10),d['Rings'].head(10))

fig=plt.figure(figsize=(8,5))
sns.heatmap(d.head().corr(),annot=True)

sns.pairplot(d.head(),hue='Rings')

sns.pairplot(d.head())

d.head()

d.tail()

d.info()

d.describe()

d.mode().T

d.shape

d.kurt()

d.skew()

d.var()

d.isna()

d.isna().any()

d.isna().sum()

d.isna().any().sum()

sns.boxplot(d['Diameter'])

qnt=d.quantile(q=[0.25,0.75])
qnt

iqr=qnt.loc[0.75]-qnt.loc[0.25]

iqr

upper=qnt.loc[0.75]+(1.5*iqr)
upper

d['Diameter']=np.where(d['Diameter']<0.155,0.4078,d['Diameter'])
sns.boxplot(d['Diameter'])

sns.boxplot(d['Length'])

d['Length']=np.where(d['Length']<0.23,0.52, d['Length'])

sns.boxplot(d['Length'])

sns.boxplot(d['Height'])

sns.boxplot(d['Height'])

d['Height']=np.where(d['Height']<0.04,0.139, d['Height'])
d['Height']=np.where(d['Height']>0.23,0.139, d['Height'])

sns.boxplot(d['Height'])

sns.boxplot(d['Whole weight'])

d['Whole weight']=np.where(d['Whole weight']>0.9,0.82, d['Whole weight'])