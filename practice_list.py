# a = ["apple", "orange", "Bnana", 450, "Graps"]
# print(type(a))
# print(a[1])
# print(a[3])
# print(a[4])
# a.append("peech")
# print(a)
# a.insert(3, "shake")
# print(a)
# a.extend([15, 20, 25]) 
# print(a) 
book_list = [445, "Think and Grow Rich", "Napoleon Hill",  50.30]
print(book_list)
print(type(book_list))
print(len(book_list))
for x in book_list:
    print(x)
print(book_list[2])
book_list.remove(50.30)
print(book_list)
del book_list[0]  
print(book_list)