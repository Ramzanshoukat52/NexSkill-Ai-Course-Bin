import numpy as np
# --------------------------ONE D ARRY -----------------
one_d = np.array([1,2,3,4,5])
print(one_d)

# # #--------------------- 2D array ------------------------------
two_d = np.array([1,2,3,4,5]),([1,2,3,4,5])
print(two_d)

# # # ----------------------------3D array------------------ 
three_d= np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(three_d)

# # # ----------------------------NumPy Data Types-----------------------
arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

# # #------------------------ print1 to 11 array----------------- 
a = np.arange(12)

# # #------------------------ print 2D 1 to 12 but 2 row and 6 coloumn ----------------------
b = np.arange(12).reshape(2,6)

# # # --------------print 3D 1 to 12 but 3 row and 3 coloumn OR 3 he set ho gay  ----------
c = np.arange(27).reshape(3,3,3)

# #         # --------------NP  array my 0 print kerwana ho tu--------------
d = np.zeros((4,5))
print(d)

# #          # --------------NP  array my 1 print kerwana ho tu--------------
e = np.ones((4,5))
print(e)

        # -----------------------np.random.random(10)--------------------------
# #      ----------------------random number print kerwana iska kanm --------------
f = np.random.random(10)
print(f)

# # vlaues print kewaan  1 sy satart hona 10 teq end or total 1sy 10 my 4 valus print ho bas output =1,2,7,10
g = np.linspace(1,10,4)
print(g)

# -----------------------------np.identity---------------------
# # -------------Matric jaha one print kerna oppostie shape my ------------------
# #  [0. 1. 0. 0. 0.]
# #  [0. 0. 1. 0. 0.]
# #  [0. 0. 0. 1. 0.]
# #  [0. 0. 0. 0. 1.]]
# # h = np.identity(5)
# # print(h)

# # ----------------------------------------Attributes-------------------------------------
# # ndim btata hain ky array oneD hain 2 D ahin 3 D OR SO ON ...yeah NDIM number of dimatiocanial btata hain  1D 2D 3D 
print(a.ndim)

# # Yeah batata hian 1d hain 2d yeah 3d my btata hain kitny column or kitny row hain 
print(b.shape)
 
# #  yeah batata hian array my kitny item hain woh btata 
print(a.size)

# # yeah item size btata hain ky item memory my kitne memory occupaay kerta ha9in 
print(a.itemsize)

# # yeah btata data ky deatial means int hain float hain chara kitny memry lay rha 32 yeah 64
print(b.dtype)

# # -------------------------------------------------Changing datatype-----------------------------------
 
# # yeah lgany sy space kam legti hain memory my 
print(i.astype)



# # ---------------------------------Dot Product-----------------------------------------------------------
# # dot matric teb he possible hona jeb a3 reshame my (3,4) or next a4 my (4,3 ) matlb  first my end wala digt or second ()my first wala same ho (3,"4")("4"e,3)  
a3 = np.arange(12).reshape(3,4)
a4 = np.arange(12).reshape(4,3)
np.dot(a3,a4)


# # ------------------------------------indexing ------------------------------------------
a5 = np.arange(10)
a6 = np.arange(12).reshape(3,4)
a7 = np.arange(8).reshape(2,2,2)
print(a6)

# # # [[ 0  1  2  3]
# # #  [ 4  5  6  7]
# # #  [ 8  9 10 11]]

print("new")
# # # output only 6...[1,2] means first row and 2 column
print(a6[1,2])


# # ---------------3D my sy index niklana -----------
print(a7)
# # [[[0 1]             ..............0  index diamticnal 
# #   [2 3]]

# #  [[4 5]               ............... 1 index diamatinol
# #   [6 7]]]
print("New 3d INDEXX")
# # [1,1,1]   1 mweans first index dimational or next 1 meeans row and then next 1 colmun 
print(a7[1,1,1])
# # ---------------------------------silacingp-----------------------
# # 1D array → a[index]
# # 2D array → a[row, column]
# # 3D array → a[layer, row, column]

a8 = np.arange(10)
a9 = np.arange(12).reshape(3,4)
a10 = np.arange(8).reshape(2,2,2)
# print(a8)
# # # [0 1 2 3 4 5 6 7 8 9]

# # # [2 3]
# # # silacing..
print(a8[2:4])


# # -------------2d---------# 2D array → a[row, column]
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]
print(a9)
# # # [ 8  9 10 11] 2 measn index 2 row hain : ka matlb sub colmn ky word 
print("\n", a9[2,:])  
# # #  [1 5 9]         : ka mtlb hain sub row ky word and 1 ka mtb 1 colomn 
print("\n", a9[:,1]) 


# # .......................3D array → a[layer, row, column]....................
a11 = np.arange(10)
a12 = np.arange(12).reshape(3,4)
a13 = np.arange(27).reshape(3,3,3)
print(a13)
# # [[[ 0  1  2]
# #   [ 3  4  5]
# #   [ 6  7  8]]

# #  [[ 9 10 11]
# #   [12 13 14]
# #   [15 16 17]]

# #  [[18 19 20]
# #   [21 22 23]
# #   [24 25 26]]
print(a13[1,1::2])
# # [[12 13 14]] 
# # yeah 12 13 13 ka mtlb ..1 index diamtional hain or  1 row hain  or :: 2 ka mtbl end teq colmn sub
print(a13[::2,1,1:3])
# # -----------------------------------loop -------------------------------------------
for i in  a13:
    print(i)

# # --------------------------Stacking-------------------
# # Adding the 2 or more  numbay  in horsizental or verticallly   
a14 = np.arange(12).reshape(3,4)
a15 = np.arange(12).reshape(3,4)
print(np.hstack((a14,a15)))
# # [[ 0  1  2  3  0  1  2  3]
# #  [ 4  5  6  7  4  5  6  7]
# #  [ 8  9 10 11  8  9 10 11]]
print(np.vstack((a14,a15)))
# # adding in vertidcally stacking
# # [[ 0  1  2  3  0  1  2  3]
# #  [ 4  5  6  7  4  5  6  7]
# #  [ 8  9 10 11  8  9 10 11]]
# # [[ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]
# #  [ 0  1  2  3]
# #  [ 4  5  6  7]
# #  [ 8  9 10 11]]

# # --------------------------splilting-------------------------
a16 = np.arange(16).reshape(4,4)
a17 = np.arange(16,32).reshape(4,4)
# # (a16,4) 4 ka mtlb kitny part my devide kerna hain  horizentlly
print(np.hsplit(a16,4))

# # (a16,4) 2 ka mtlb kitny part my devide kerna hain vertically  
print(np.vsplit(a16,2))