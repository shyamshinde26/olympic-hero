# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data=pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'},inplace=True)
data.head(10)


# --------------
#Code starts here
data['Better_Event']=np.where(data['Total_Summer']>data['Total_Winter'],'Summer','Winter')
data['Better_Event'] = np.where(data['Total_Summer'] == data['Total_Winter'] , 'Both', data['Better_Event'])
better_event=data['Better_Event'].value_counts().idxmax()
print(better_event)


# --------------
#Code starts here
top_countries=data[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']]
top_countries.drop(top_countries.tail(1).index,inplace=True, axis=0)
def top_ten(DF,lst):
    Country_list=[]
    top=DF.nlargest(10, lst)
    Country_list=top['Country_Name']
    return list(Country_list)
top_10_summer=top_ten(top_countries,'Total_Summer')
top_10_winter=top_ten(top_countries,'Total_Winter')
top_10=top_ten(top_countries,'Total_Medals')
common=list(set(top_10_summer) & set(top_10_winter) & set(top_10))





# --------------
#Code starts here
data.drop(data.tail(1).index,inplace=True, axis=0)
summer_df=data[data['Country_Name'].isin(top_10_summer)]
winter_df=data[data['Country_Name'].isin(top_10_winter)]
top_df=data[data['Country_Name'].isin(top_10)]
plt.bar(data['Country_Name'],data['Total_Summer'])
plt.bar(data['Country_Name'],data['Total_Winter'])
plt.bar(data['Country_Name'],data['Total_Medals'])


# --------------
#Code starts here
summer_df.set_index('Country_Name',inplace=True)
summer_df['Golden_Ratio']=summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_df['Golden_Ratio'].round(2)
summer_max_ratio=summer_df.max()['Golden_Ratio']
summer_country_gold=summer_df['Golden_Ratio'].idxmax()
print(summer_country_gold)

winter_df.set_index('Country_Name',inplace=True)
winter_df['Golden_Ratio']=winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_df['Golden_Ratio'].round(2)
winter_max_ratio=winter_df.max()['Golden_Ratio']
winter_country_gold=winter_df['Golden_Ratio'].idxmax()
print(winter_country_gold)

top_df.set_index('Country_Name',inplace=True)
top_df['Golden_Ratio']=top_df['Gold_Total'] / top_df['Total_Medals']
top_df['Golden_Ratio'].round(2)
top_max_ratio=top_df.max()['Golden_Ratio']
top_country_gold=top_df['Golden_Ratio'].idxmax()
print(summer_country_gold)


# --------------
# Code starts here
data_1=data.drop(data.tail(1).index)
data_1['Total_Points'] = (data_1['Gold_Total'].astype(int)*3 + data_1['Silver_Total'].astype(int)*2 + data_1['Bronze_Total'].astype(int)*1)
most_points=max(data_1['Total_Points'])
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']



# --------------
#Code starts here
best=data[data['Country_Name']==best_country]
# print(data_2)
best=best.iloc[: , 12:15]
best.plot.bar(width=0.3)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)
plt.title('bar graph')
plt.show()


