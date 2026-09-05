import pandas as pd
data = pd.read_csv("RealEstate-USA.csv")
print(data)
# ------------------------serios of list--------------
# S_list = ['pakiatn', 'UEA', 'UK', 'USA', 'INDAI']
# # 0    pakiatn
# # 1       UEA
# # 2       UK
# # 3       USA
# # 4      INDAI
# # dtype: str
# # pandas serois my counting leg ge intex ke foram my 
# print("This is Serous list:\n",pd.Series(S_list))

# # ---------------------------serios my index (counding khatm kerna or khud sy index name dain ).........
# marks = [80,70,40,60,70]
# sub = ['English', 'Urdu', 'Mathe', 'computer', 'information Security']
# result= pd.Series(marks, index= sub, name = 'The Final Result of : Haroon',)
# print("This is Series of converd Index own Values:\n",result)

# # -------------------------------Attributes---------------------------------
# #                                 .size
# # print(len(result))
# print("The Total size of Result:\n",result.size)
#                                 #   .dtype

# print("The Datatype of Series:\n",result.dtype)
# #                                   .name
# print("The Name we show end the result:\n",result.name)
# # The Final Result of : Haroon

# #                                   .is_unique 
# print("Tell the values is Uniques:\n",result.is_unique)
# # ager koie be valyes same howei tu result my true aye ga other wise false

# print("This is know the indes the :\n",result.index)
# # Index(['English', 'Urdu', 'Mathe', 'computer', 'information Security'], dtype='str')

# print("This is know the vlaues :\n",result.values)
# # [80 70 40 60 70]

# # -----------------------------------info()-------------------------
# print("df.info():   " , result.info() )
# # To df.info() ye batata hai:
# # Kitni rows hain.
# # Kitne columns hain.
# # Har column ka data type (dtype) kya hai.
# # Har column mein kitni non-null values hain.
# # Memory kitni use ho rahi hai.

# # -----------------------------------head ()---------------------------------------
# # randam data show kerwata row my kesy datat show hota
# print("This is head of values:\n",data.head())
# # -------First top 2 row data show----------------
# print("This is head of values:\n",data.head(2))


# # -----------------------------------tail ()---------------------------------------
# print("This is head of values:\n",data.tail())
# # -------end  2 row data show----------------
# print("This is head of values:\n",data.head(2))

# # -------------------------------------describe()-----------------------------
# print("Summary of Statistics operation like mean meadain mode etd...:", data.describe())

# # ------------------------------------------------shape---------------------------
# print("Counting the rows and columns in DataFrame using shape() : " ,data.shape)


# # ---------------------------------Access the Name column-------------------------------- 
# col=data['city']
# print("The name of colmun acces in data single column:",col)

# # ---------------------------------Access the Multiplate Column  in  Name -------------------------------- 

# col_multiplae= data[['city','street']]
# print("Acces the Multiplae column :",col_multiplae)



# # ---------------------------------Access the Name ROW usng loc()-------------------------------- 

# row=data.loc[4]
# print("The name of row acces in data single column:",row)


# # ---------------------------------Access the Multiplate row in  Name -------------------------------- 
# row_multiplae= data.loc[[4,3]]
# print("\nAcces the Multiplae column :",row_multiplae)


# # -------------------------selecting the slicing using lock---------------------
# slic_data= data.loc[2:4]
# print("#Selecting a slice of rows using .loc",slic_data)


#-----------------Conditional selection of rows using .loc------------
# jaha jaha data my city colomn my "ponce" ho ga woh all row ko utah ly ga
condistion_row = data.loc[data['city'] == 'Ponce']
print("Conditional selection of rows using .loc",condistion_row)





