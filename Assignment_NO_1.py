# Question 1: 
# Write a program that converts a temperature from Celsius to Fahrenheit. 
# print("----- The Celsius to Fahrenheit values-----")
# celsius = float(input("Enter The values:"))
# Fahrenheit = celsius * 9/5 + 32
# print(Fahrenheit)

# Question 2: 
# Calculate Area of a Rectangle
# print("-----Calculate Area of a Rectangle-----")
# l = int(input("Enter the Lenght:"))
# w = int(input("Enter the Width:"))
# total = w * l
# print("The Total Area is :",total)


# Question 3: 
# Calculate Compound Interest
# Use the formula: 
# CI = P * (1 + R/100)**T - P 
# Where P = principal, R = rate, T = time
# print("-----Calculate Compund Interest-----")
# principal = float(input("Enter The Principal:"))
# rate = float(input("Enter The Rate:"))
# time = float(input("Enter The Time:"))
# CI = principal * (1 + rate/100)**time - principal
# print("The Total Compound is :",CI) 

# Question 4: 
# Perimeter of a Rectangle - Take length and width as input and calculate the perimeter. 
# Calculate Area of a Rectangle
# print("-----Perimeter Rectangle-----")
# l = int(input("Enter the Lenght:"))
# w = int(input("Enter the Width:"))
# perimeter = 2 * (w + l)
# print("Perimeter Tectangle is :",perimeter)


# Question 5: 
# Average of Three Numbers - Input three numbers and print their average. 

# print("-----Welcome The calculate Thre values average-----")
# a = int(input("Enter the First values:"))
# b = int(input("Enter the Second values:"))
# c = int(input("Enter the Thired values:"))
# average = a + b + c / 3
# print("The Total Average of Theree Number is:",average)

# Question 6: 
# Square and Cube of a Number - Ask the user for a number and display its square and cube.

# print("-----Welcome Calcualte The Square and Cube The number-----")
# number = int(input("Enter The Square and Cube value:"))
# square = number * number
# cube = number * number * number
# print("The Sqare is:",square)
# print("The Cube is :",cube)

# Question 7: 
# Distribute Items Equally - You have n candies and k students. 
# Write a program to find: 
# how many candies each student gets 
# how many are left 

# candies = int(input("Enter The candies:"))
# student = int(input("Enter The students:"))
# div = candies / student
# reminder = candies % student
# print("Candies each studnet:",div)
# print("Total canides Left",reminder)


# Question 8: 
# Calculate Profit or Loss 
# Input cost price and selling price. Display either: 
# Profit and amount, or 
# Loss and amount, or 
# No Profit No Loss

# print("-----Welcome Calculate Profit or Loss-----")
# cost_price = int(input("Enter The Cost Price:"))
# seling_price = int(input("Enter The seling Price:"))
# if seling_price > cost_price:
#     pro = seling_price - cost_price
#     print("We are profit:") 
#     print("The Total Profit is:",pro) 
# elif seling_price < cost_price:
#     loss = cost_price - seling_price
#     print("We are losss:")
#     print ("The Total loss is:",loss)
# else:
#     print("NO loss No Profit")

# # Question 9: 
# # Total Marks and Percentage 
# # Input marks of 5 subjects. Print: 
# #  Total marks 
# #  Percentage 
# #  Average 

# print("-----Welcome calculate The Student Result -----")
# english = int(input("Enter The English Marks:"))
# urdu = int(input("Enter The URDU Marks:"))
# Bio = int(input("Enter The Biology Marks:"))
# Com = int(input("Enter The Computer Marks:"))
# Math = int(input("Enter The Mathematics Marks:"))
# total = english + urdu + Bio + Com + Math 
# per = total / 500 * 100
# avg = total / 5
# print("The Total Marks is:",total)
# print("The Percentage is:",per)
# print("The Averge of student Result is :",avg)

# Question 10: 
# Salary Calculator 
# Input basic salary. Calculate: 
#  HRA = 20% of basic 
#  DA = 15% of basic 
#  Total Salary = Basic + HRA + DA

# print("-----Welcome Calculate the Salary-----")
# b_salry = int(input("Enter the Basic Salry:"))
# HRA = b_salry  * 20 / 100
# DA = b_salry  * 15 / 100
# Total_salry = b_salry  + HRA + DA
# print("The Total HRA Allowance :",HRA)
# print("The Total DA Allowance :",DA)
# print("The Total Salry is :",Total_salry)

# Question 11: 
# Age in Months and Days 
# Input your age in years. Calculate and print age in: 
#  Months 
#  Days (approximate) 
# from datetime import datetime
# print("-----Welcome Calculate Age month and Day-----")
# year = int(input("Enter The year:"))
# month = int(input("Enter The Month:"))
# day = int(input("Enter The day:"))
# today = datetime.now()
# age_year = today.year - year
# age_month = today.month - month
# age_day = today.day - day
# print("The age is :",age_year) 
# print("The month is :",age_month) 
# print("The day is :",age_day) 


# # Question 12: 
# # Currency Converter (USD to PKR) 
# # Input amount in USD. Convert using a fixed exchange rate. 

# print("-----Welcome Calculate USD TO PKR-----")
# converter_amount = int(input("Enter The USD To converd into PKR:"))
# USD = 280
# PKR = USD * converter_amount
# print("The Total Amount of USD TO PKR is:",PKR)

# Question 13: 
# Sum of First N Natural Numbers 
# Input a number n, calculate sum of first n natural numbers. 
# Formula: sum = n * (n + 1) / 2

# print("-----Welcome calculate Natural Number Sum-----")
# n = int(input("Enter the Natural Number:"))
# sum = n * (n + 1) / 2
# print("The sum of :",sum)




