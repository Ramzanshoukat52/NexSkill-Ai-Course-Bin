import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import plotly.express as px


# ****************************imort kiya hain data using sns.load_dataset('tips') seaborn sy*****************
# tips = sns.load_dataset('tips')
# print(tips)



# # *******************************************Scator ploat axies level ******************************
# first_a=sns.scatterplot(data= tips ,x = 'total_bill', y = 'tip',hue='sex',style='time',size='size',style='sex',)

# print(first_a)
# plt.show() 


# # *******************************************Scator ploat  figure level ******************************
# row='smoker',col= 'sex' only run in scator plaot figure level ...
# first_b=sns.relplot(data= tips ,x = 'total_bill', y = 'tip',kind = 'scatter',hue='sex',style='time',size='size',style='sex',row='smoker',col= 'sex',col_wrap= 2)
# print(first_b)
# plt.show() 



# # *******************************************line ploat axies level ******************************
# second_a=sns.lineplot(data= tips ,x = 'size', y = 'smoker',style='sex', )
# print(second_a)
# plt.show() 


# # *******************************************line ploat  figure level ******************************
# second_b=sns.relplot(data= tips ,x = 'size', y = 'smoker',kind = 'line',row='smoker',col= 'sex',col_wrap= 2)
# # row='smoker',col= 'sex' only run in line plaot figure level ...
# print(second_b)
# plt.show() 





# ******************************Distributaion Ploat******************************************
# ✅ histplot()
# ✅ kdeplot()
# ✅ rugplot()

# titanic_data = sns.load_dataset('titanic')
# print(titanic_data)
# sns.displot(data=titanic_data, x= 'age', kind ='hist',hue='sex',element='step')
# plt.show()


# *************************************kdeplot()**********************************
# ismay count ni ata y axies per ismy dinesty show hote....0.5 0.2.0.4.0.5

# kdeplot_graph = sns.displot(data = tips, x = 'total_bill',kind='kde',hue='sex', fill='True')
# print(kdeplot_graph)
# plt.show()



# *************************************rugplot()**********************************

# f_graph = sns.kdeplot(data = tips, x = 'total_bill')
# se_graph = sns.rugplot(data = tips, x = 'total_bill')
# # nichy x axies per choti choti lines jo show ho ri hain woh rugplot ka kam hain 
# print(f_graph)
# print(se_graph)
# plt.show()



# ***********************************matric ploat*************************
# --> headmap
# --> clustermap
# gap = px.data.gapminder()
# print(gap)
# heat_map = gap.pivot(index='country',columns = 'year', values= 'lifeExp')
# # ---> pivot() data ko long format se wide format mein convert karta hai — matlab rows ko columns mein "ghumana" (pivot karna).
# plt.figure(figsize=(5,5))
# sns.heatmap(heat_map)
# plt.show()


# ************************** heat_map ----->  annot map****************
# heat_map = gap[gap['continent'] == 'Europe'].pivot(index='country', columns='year', values='lifeExp')
# plt.figure(figsize=(5,5))
# sns.heatmap(heat_map,annot=True,linewidths=0.5,cmap='summer')
# annot=True (annotate)
# Har cell ke andar uski actual numeric value likh deta hai

# linewidths=0.5
# Cells ke beech mein thin white lines (border) add karta hai
# plt.show()


#  *****************************************headmap under *****************************
# *****************************************clustermap*****************************

new_data=px.data.iris()
print(new_data)
