import pandas as pd

data = pd.read_csv("RealEstate-USA.csv")
data1 = pd.read_csv("RealEstate-USA.csv")

print(data)
# # ........................shape---------------- 
# # --------------------------tell how many  row and column in datafram--------------- 
# print((data.shape))

# # ........................dtype---------------- 
# print(data.dtypes)

# # ........................index---------------- 
# print(data.index)

# # ........................index_define name ----------------
# # ------------------------yeah index 123 ko khatam kerta ho jo values day usjko index bna daita hain -=--- 
# print(data.set_index('status'))

# # ........................column---------------- 
# # ------------------------tell the column name ------------------
# print(data.columns)

# # ........................values---------------- 
# print(data.values)

# # ........................head---------------- 
# print(data.head(2))

# # ........................tail---------------- 
# print(data.tail(2))

# # ........................samole---------------- 
# print(data.sample)

# ........................info---------------- 
# ------------------------data ky bary my btata ro colmn memry kite occupay datatype sub chesy batat----------------
# print(data.info())

# .......................Decribe---------------- 
# --------------statistis opertaion --------------------
# print(data.describe())

# ........................isnull---------------- 
# ----------------------dataframe my dehkhta kaha kaha per values miss hain ---------true false ke foram my 
# print(data.isnull())

# ........................dublicate---------------- 
# print(data.duplicated())

# ........................rename---------------- 
# -------------------inplace TURE measn dataframe my permanent change ker dy ga price rs my ---
# data.rename(columns={'price': 'RS'}, inplace=True)
# print(data)


# ----------------------mathmatical operation --------------------
# -------------------------singel colmun sum()
# data.sum() ya data.sum(axis=0) → Column-wise sum
# data.sum(axis=1) → Row-wise sum
# print(data['price'].sum())

# ************************Column ****************************
# ...................single column fetch----------------
# ...................single or multiplae  column fetch----------------
# print(data[['city','bath']])




# ************************Row ****************************
# loc = Label (naam)
# iloc = Integer (number) ........*****index sy target hota [0,1,2] 
print(data.iloc[2])

# ******************multi row fatch using ilock **************
print(data.iloc[1:5])



# *******************row fatch using loc****************
# loc = Label (naam)

print(data.loc[[2,3]])

# *******************row and column  fatch using loc****************
print(data.loc[[2, 3], ['price', 'bed']])