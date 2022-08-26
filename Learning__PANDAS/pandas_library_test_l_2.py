import pandas as pd

Mobile_data = pd.read_csv("C:/Users/User/Desktop/MACHINE LEARNING/DATA/test.csv")
print(Mobile_data.iloc[0])
print(Mobile_data.iloc[:5, 1])
print(Mobile_data.iloc[:5, [1,2,3]])
print('\n\n')
print(Mobile_data.loc[:5, ['id','battery_power','blue']])
Mobile_data.set_index("battery_power")
print(Mobile_data.head(15))
print(Mobile_data.loc[Mobile_data.blue == 1])