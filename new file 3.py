
book_year = 1998
book_price = 54.5
result = int(book_year * book_price)
print("The result is:", result)
print(type(result))
if book_price > 50:
    print("Expensive book")
elif book_price < 50 :
    print("Reasonable BOOK")
else:
    print("Not avaibale ")