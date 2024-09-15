import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv(r'C:\Users\Owner\Documents\me_files\pyth files\insurance.csv')

print(data.dtypes,'\n')
print(data.shape,'\n')
print('Checking for missing values:\n', data.isna().sum(),'\n')

column0=['smoker','region','sex']
column=['age','children','bmi']

for i in column0:
    sns.countplot(x=i, data=data)
    plt.show()


for i in column:
    x=data[i]
    y=data['charges']
    plt.scatter(x,y)
    plt.xlabel(i)
    plt.ylabel("Charges")
    plt.show()

sns.pairplot(data)
plt.show()
data1=pd.read_excel(r'C:\Users\Owner\Documents\me_files\pyth files\only_smokers.xlsx')

sns.regplot(x='age',y='charges',data=data1)
plt.ylim(0,)

plt.show()












